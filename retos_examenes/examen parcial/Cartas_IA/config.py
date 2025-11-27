import numpy as np

class Config:
    CARD_W = 200
    CARD_H = 300

    GREEN_LOWER = np.array([35, 50, 50])
    GREEN_UPPER = np.array([90, 255, 255])
    MIN_GREEN_RATIO = 0.25

    MIN_CARD_AREA = 5000
    MAX_CARD_AREA = 350000

    # Esquina superior derecha
    CORNER_X1 = 0
    CORNER_Y1 = 0
    CORNER_X2 = CARD_W
    CORNER_Y2 = CARD_H

    # ===== ROIs DEFINITIVAMENTE CALIBRADAS =====
    VAL_ROI  = (20, 20, 55, 55) 
    SUIT_ROI = (45, 65, 55, 55)   

    VALUE_MATCH_THRESH = 0.30
    SUIT_MATCH_THRESH  = 0.30

    DEBUG = True

def debug_print(*args, **kwargs):
    if Config.DEBUG:
        print(*args, **kwargs)
