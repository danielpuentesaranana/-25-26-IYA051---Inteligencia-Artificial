import cv2
import numpy as np

from config import Config, debug_print
from segmenter import Segmenter
from detector import CardDetector
from templates import TemplateManager


def suit_to_spanish(s):
    return {
        "hearts":   "corazones",
        "diamonds": "diamantes",
        "clubs":    "tréboles",
        "spades":   "picas"
    }.get(s, s)


class CardRecognizer:
    def __init__(self):
        self.seg = Segmenter()
        self.det = CardDetector()
        self.tpl = TemplateManager()

    # ===============================================================
    #  ROTACIÓN ROBUSTA: PRUEBA 0º, 90º, 180º, 270º Y ELIGE LA MEJOR
    # ===============================================================
    def _rotate(self, img, angle):
        if angle == 0:
            return img
        elif angle == 90:
            return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            return cv2.rotate(img, cv2.ROTATE_180)
        elif angle == 270:
            return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            return img

    def force_best_rotation(self, warp):
        best_img = warp
        best_score = -1

        for angle in [0, 90, 180, 270]:
            rotated = self._rotate(warp, angle)

            # esquina donde se supone que están valor+palo
            corner = rotated[
                Config.CORNER_Y1:Config.CORNER_Y2,
                Config.CORNER_X1:Config.CORNER_X2
            ]

            if corner.size == 0:
                continue

            gray = cv2.cvtColor(corner, cv2.COLOR_BGR2GRAY)
            # invertimos para contar "tinta" oscura
            _, th = cv2.threshold(gray, 0, 255,
                                  cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            ink_score = cv2.countNonZero(th)

            if ink_score > best_score:
                best_score = ink_score
                best_img = rotated

        debug_print(f"[ROT] mejor rotación, tinta={best_score}")
        return best_img

    # ===============================================================
    #   RECONOCIMIENTO DE CARTAS
    #   calibration_mode=True -> primero calibra ROIs en ese frame
    # ===============================================================
    def recognize_cards_in_frame(self, frame_bgr, calibration_mode=False):
        mask = self.seg.get_mask(frame_bgr)
        contours = self.det.find_card_contours(mask)
        results = []

        if not contours:
            debug_print("[RECOGNIZER] No se encontraron cartas")
            return results

        for i, c in enumerate(contours):
            quad = self.det.contour_to_quad(c)
            warp = self.det.warp_card(frame_bgr, quad)

            # usar nuestra rotación robusta
            warp = self.force_best_rotation(warp)

            # ---------- MODO CALIBRACIÓN ----------
            if calibration_mode and i == 0:
                val_roi_cfg, suit_roi_cfg = self.calibrate_rois_interactively(warp)

                # Si el usuario canceló con ESC
                if val_roi_cfg is None or suit_roi_cfg is None:
                    debug_print("[CALIBRACIÓN] Cancelada por el usuario")
                    return []

                Config.VAL_ROI = val_roi_cfg
                Config.SUIT_ROI = suit_roi_cfg

                debug_print(f"[CALIBRACIÓN] VAL_ROI  = {Config.VAL_ROI}")
                debug_print(f"[CALIBRACIÓN] SUIT_ROI = {Config.SUIT_ROI}")
            # --------------------------------------

            # Cortar la esquina donde están valor/palo
            corner = warp[
                Config.CORNER_Y1:Config.CORNER_Y2,
                Config.CORNER_X1:Config.CORNER_X2
            ]

            if corner.size == 0:
                continue

            vx, vy, vw, vh = Config.VAL_ROI
            sx, sy, sw, sh = Config.SUIT_ROI

            roi_val  = corner[vy:vy+vh, vx:vx+vw]
            roi_suit = corner[sy:sy+sh, sx:sx+sw]

            # Guardar ROIs para crear plantillas si quieres
            try:
                cv2.imwrite("debug_val_roi_0.png", roi_val)
                cv2.imwrite("debug_suit_roi_0.png", roi_suit)
            except:
                pass

            # Matching con plantillas
            val, s_val = self.tpl.match_value(roi_val)
            sui, s_sui = self.tpl.match_suit(roi_suit)

            debug_print(f"[MATCH] val={val}({s_val:.2f})  suit={sui}({s_sui:.2f})")

            # De momento, acepta SIEMPRE el mejor (ya filtrarás con umbral si quieres)
            val_final = val
            sui_final = sui

            results.append({
                "contour": c,
                "quad": quad,
                "value": val_final,
                "suit": sui_final
            })

        return results

    # ===============================================================
    #              CALIBRACIÓN INTERACTIVA DE ROIs
    # ===============================================================
    def calibrate_rois_interactively(self, warp):
        # Partimos de los valores actuales
        val_x, val_y, val_w, val_h = Config.VAL_ROI
        suit_x, suit_y, suit_w, suit_h = Config.SUIT_ROI

        print("\n=== MODO CALIBRACIÓN ACTIVADO ===")
        print("Mover ROI valor (AZUL):  W,S,A,D | Q/E (ancho)  Z/X (alto)")
        print("Mover ROI palo  (ROJO):  I,K,J,L | U/O (ancho)  N/M (alto)")
        print("Pulsa G para imprimir coordenadas.")
        print("Pulsa ENTER para ACEPTAR, ESC para CANCELAR.\n")

        while True:
            dbg = warp.copy()

            # Esquina completa
            cv2.rectangle(
                dbg,
                (Config.CORNER_X1, Config.CORNER_Y1),
                (Config.CORNER_X2, Config.CORNER_Y2),
                (0, 255, 0), 2
            )

            # ROI Valor (azul)
            cv2.rectangle(
                dbg,
                (Config.CORNER_X1 + val_x, Config.CORNER_Y1 + val_y),
                (Config.CORNER_X1 + val_x + val_w, Config.CORNER_Y1 + val_y + val_h),
                (255, 0, 0), 2
            )

            # ROI Palo (rojo)
            cv2.rectangle(
                dbg,
                (Config.CORNER_X1 + suit_x, Config.CORNER_Y1 + suit_y),
                (Config.CORNER_X1 + suit_x + suit_w, Config.CORNER_Y1 + suit_y + suit_h),
                (0, 0, 255), 2
            )

            cv2.imshow("ROI CALIBRATION", dbg)
            k = cv2.waitKey(1) & 0xFF

            # ESC -> cancelar
            if k == 27:
                cv2.destroyWindow("ROI CALIBRATION")
                print("\n[CALIBRACIÓN] Cancelada con ESC\n")
                return None, None

            # ENTER -> aceptar
            if k in (13, 10):
                cv2.destroyWindow("ROI CALIBRATION")
                print("\n[CALIBRACIÓN] Aceptada.")
                print("VAL_ROI  =", (val_x, val_y, val_w, val_h))
                print("SUIT_ROI =", (suit_x, suit_y, suit_w, suit_h))
                print()
                return (val_x, val_y, val_w, val_h), (suit_x, suit_y, suit_w, suit_h)

            # ------- CONTROLES ROI VALOR (AZUL) -------
            if k == ord('w'): val_y -= 2
            if k == ord('s'): val_y += 2
            if k == ord('a'): val_x -= 2
            if k == ord('d'): val_x += 2
            if k == ord('q'): val_w -= 2
            if k == ord('e'): val_w += 2
            if k == ord('z'): val_h -= 2
            if k == ord('x'): val_h += 2

            # ------- CONTROLES ROI PALO (ROJO) -------
            if k == ord('i'): suit_y -= 2
            if k == ord('k'): suit_y += 2
            if k == ord('j'): suit_x -= 2
            if k == ord('l'): suit_x += 2
            if k == ord('u'): suit_w -= 2
            if k == ord('o'): suit_w += 2
            if k == ord('n'): suit_h -= 2
            if k == ord('m'): suit_h += 2

            # Mostrar coordenadas actuales
            if k == ord('g'):
                print("\n======= COORDENADAS ACTUALES =======")
                print(f"VAL_ROI  = ({val_x}, {val_y}, {val_w}, {val_h})")
                print(f"SUIT_ROI = ({suit_x}, {suit_y}, {suit_w}, {suit_h})")
                print("====================================\n")

    # ===============================================================
    #              DIBUJAR RESULTADOS EN LA IMAGEN
    # ===============================================================
    def draw_results(self, img, results):
        out = img.copy()
        for r in results:
            c = r["contour"]
            v = r["value"]
            s = r["suit"]

            cv2.drawContours(out, [c], -1, (0, 255, 0), 2)

            if v and s:
                text = f"{v} de {suit_to_spanish(s)}"
            elif v:
                text = v
            else:
                text = "Desconocida"

            x, y = c[0][0]
            cv2.putText(
                out,
                text,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )

        return out
