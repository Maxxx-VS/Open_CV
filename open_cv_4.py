import cv2
import numpy as np


cap = cv2.VideoCapture('videos/sample.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('POTOK', img)


    # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) # половина от размера
    img = cv2.GaussianBlur(img, (9, 9), 0) # размытие
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # ч/б оттенки

    img = cv2.Canny(img, 30, 30) # бинарная (ч/б - 1,0)

    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1) # ширина точек (обводка)

    img = cv2.erode(img, kernel, iterations=1)

    cv2.imshow('POTOK', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

