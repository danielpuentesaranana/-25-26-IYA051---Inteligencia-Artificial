import cv2
import numpy as np
from config import Config, debug_print

def order_points(pts):
    pts = np.array(pts, dtype="float32")
    s = pts.sum(axis=1)
    tl = pts[np.argmin(s)]
    br = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    tr = pts[np.argmin(diff)]
    bl = pts[np.argmax(diff)]
    return np.array([tl, tr, br, bl], dtype="float32")

class CardDetector:
    def find_card_contours(self, mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cand = []
        for c in contours:
            area = cv2.contourArea(c)
            if Config.MIN_CARD_AREA < area < Config.MAX_CARD_AREA:
                cand.append(c)
        debug_print(f"[DETECTOR] {len(cand)} candidatos")
        return cand

    def contour_to_quad(self, contour):
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) >= 4:
            hull = cv2.convexHull(approx)
            pts = hull.reshape(-1, 2)
            if len(pts) > 4:
                rect = cv2.minAreaRect(pts)
                box = cv2.boxPoints(rect)
                pts = np.array(box, dtype="float32")
            return order_points(pts)

        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        return order_points(box)

    def warp_card(self, frame_bgr, quad):
        dst = np.array([
            [0, 0],
            [Config.CARD_W-1, 0],
            [Config.CARD_W-1, Config.CARD_H-1],
            [0, Config.CARD_H-1]
        ], dtype="float32")

        M = cv2.getPerspectiveTransform(quad, dst)
        return cv2.warpPerspective(frame_bgr, M, (Config.CARD_W, Config.CARD_H))

    def best_rotation_for_corner(self, img):
        best = img
        best_score = -1
        best_angle = 0
        sx, sy, sw, sh = Config.SUIT_ROI

        for ang in [0,90,180,270]:
            if ang == 0:  r = img
            elif ang == 90: r = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            elif ang == 180: r = cv2.rotate(img, cv2.ROTATE_180)
            else: r = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

            gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
            corner = gray[Config.CORNER_Y1:Config.CORNER_Y2,
                          Config.CORNER_X1:Config.CORNER_X2]

            if corner.size == 0:
                continue

            _, th = cv2.threshold(corner, 0, 255,
                                  cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            roi = th[sy:sy+sh, sx:sx+sw]
            score = cv2.countNonZero(roi)

            if score > best_score:
                best_score = score
                best = r
                best_angle = ang

        debug_print(f"[DETECTOR] rotación final={best_angle}, tinta={best_score}")
        return best
