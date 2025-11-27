import cv2
import numpy as np
from config import Config, debug_print

class Segmenter:
    def mask_from_green_background(self, frame_bgr):
        hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)
        mask_green = cv2.inRange(hsv, Config.GREEN_LOWER, Config.GREEN_UPPER)
        mask_not_green = cv2.bitwise_not(mask_green)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask_not_green = cv2.morphologyEx(mask_not_green, cv2.MORPH_OPEN, kernel)
        mask_not_green = cv2.morphologyEx(mask_not_green, cv2.MORPH_CLOSE, kernel)
        return mask_not_green

    def mask_from_edges(self, frame_bgr):
        gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150)
        edges = cv2.dilate(edges, None, iterations=2)
        return edges

    def choose_mask(self, frame_bgr):
        hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)
        mask_green = cv2.inRange(hsv, Config.GREEN_LOWER, Config.GREEN_UPPER)

        ratio = cv2.countNonZero(mask_green) / (frame_bgr.shape[0] * frame_bgr.shape[1])
        debug_print(f"[SEG] ratio green: {ratio:.3f}")

        if ratio > Config.MIN_GREEN_RATIO:
            return self.mask_from_green_background(frame_bgr)
        return self.mask_from_edges(frame_bgr)

    def get_mask(self, frame_bgr):
        return self.choose_mask(frame_bgr)
