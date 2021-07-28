import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('orignal frame', frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_orange = np.array([2, 50, 50])
    high_orange = np.array([20, 255, 255])

    mask = cv2.inRange(hsv, low_orange, high_orange)
    cv2.imshow('Masked Frame', mask)

    result1 = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('result', result1)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()