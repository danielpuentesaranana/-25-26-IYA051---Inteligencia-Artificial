import cv2
from recognizer import CardRecognizer

class App:

    def __init__(self):
        self.rec = CardRecognizer()

    def run_photo(self, path):
        img = cv2.imread(path)
        if img is None:
            print("No se pudo cargar:", path)
            return

        results = self.rec.recognize_cards_in_frame(img)
        out = self.rec.draw_results(img, results)

        cv2.imshow("Resultado", out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run_webcam_capture(self, cam_index=0):
        cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)

        if not cap.isOpened():
            print("Webcam no disponible")
            return

        print("Pulsa C para CALIBRAR+RECONOCER, R para RECONOCER directo, ESC para salir.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("Vista previa", frame)
            k = cv2.waitKey(1) & 0xFF

            # ---- CALIBRAR + RECONOCER EN LA MISMA FOTO ----
            if k == ord('c'):
                print("\n[CALIBRACIÓN] usando frame actual...")
                results = self.rec.recognize_cards_in_frame(frame, calibration_mode=True)
                if results:
                    out = self.rec.draw_results(frame, results)
                    cv2.imshow("Resultado", out)
                else:
                    print("[CALIBRACIÓN] No se reconoció ninguna carta (o se canceló).\n")

            # ---- SOLO RECONOCER (sin recalibrar) ----
            elif k == ord('r'):
                print("\n[RECONOCIMIENTO] usando ROIs actuales...")
                results = self.rec.recognize_cards_in_frame(frame, calibration_mode=False)
                out = self.rec.draw_results(frame, results)
                cv2.imshow("Resultado", out)

            elif k == 27:  # ESC
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = App()
    app.run_webcam_capture(1)   # cambia el índice si hace falta (0,1,2,...)
    # app.run_photo("mi_foto.jpg")

