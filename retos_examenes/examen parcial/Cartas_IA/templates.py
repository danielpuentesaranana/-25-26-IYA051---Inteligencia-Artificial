import os
import cv2
import numpy as np
from config import debug_print

class TemplateManager:
    def __init__(self, values_dir="templates/values", suits_dir="templates/suits"):
        self.values = self._load(values_dir)
        self.suits  = self._load(suits_dir)
        debug_print(f"[TPL] cargados {len(self.values)} valores y {len(self.suits)} palos")

    def _load(self, folder):
        d = {}
        if not os.path.isdir(folder):
            return d

        for f in os.listdir(folder):
            if not f.lower().endswith(("png","jpg","jpeg")):
                continue

            img = cv2.imread(os.path.join(folder,f), cv2.IMREAD_GRAYSCALE)
            if img is None: continue

            _, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            d[os.path.splitext(f)[0]] = img

        return d

    def _match(self, roi, templates):
        if roi is None or roi.size==0:
            return None, -1

        if len(roi.shape)==3:
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        _, roi = cv2.threshold(roi, 0,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        best = None
        best_s = -1

        for name, t in templates.items():
            r = cv2.resize(roi, (t.shape[1], t.shape[0]))
            res = cv2.matchTemplate(r, t, cv2.TM_CCOEFF_NORMED)
            _, m, _, _ = cv2.minMaxLoc(res)

            if m > best_s:
                best_s = m
                best = name

        return best, best_s

    def match_value(self, roi):
        return self._match(roi, self.values)

    def match_suit(self, roi):
        return self._match(roi, self.suits)
