import cv2
import numpy as np

def nothing(x):
    pass

CAM_INDEX = 1  

cap = cv2.VideoCapture(CAM_INDEX, cv2.CAP_DSHOW) 

if not cap.isOpened():
    print("No se pudo abrir la cámara en el índice", CAM_INDEX)
    exit()

cv2.namedWindow("HSV")
cv2.createTrackbar("H min", "HSV", 35, 179, nothing)
cv2.createTrackbar("S min", "HSV", 50, 255, nothing)
cv2.createTrackbar("V min", "HSV", 50, 255, nothing)
cv2.createTrackbar("H max", "HSV", 90, 179, nothing)
cv2.createTrackbar("S max", "HSV", 255, 255, nothing)
cv2.createTrackbar("V max", "HSV", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer frame de la cámara")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("H min", "HSV")
    s_min = cv2.getTrackbarPos("S min", "HSV")
    v_min = cv2.getTrackbarPos("V min", "HSV")
    h_max = cv2.getTrackbarPos("H max", "HSV")
    s_max = cv2.getTrackbarPos("S max", "HSV")
    v_max = cv2.getTrackbarPos("V max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    mask_inv = cv2.bitwise_not(mask)

    cv2.imshow("Original", frame)
    cv2.imshow("Mask verde", mask)
    cv2.imshow("Mask invertida", mask_inv)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        print("Rango HSV final:")
        print("LOWER =", lower)
        print("UPPER =", upper)
        break

cap.release()
cv2.destroyAllWindows()
