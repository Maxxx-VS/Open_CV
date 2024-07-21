import cv2
import numpy as np

# # ВЫВОД РАЗМЕРА ИЗОБРАЖЕНИЯ
# img = cv2.imread('images/ozero.jpg')
# print(img.shape)
#
# # ИЗМЕНЕНИЕ РАЗМЕРА ИЗОБРАЖЕНИЯ
# img = cv2.imread('images/ozero.jpg')
# img = cv2.resize(img, (500, 500))
# cv2.imshow('KARTINKA', img)
#
# cv2.waitKey(0)
#
# # ИЗМЕНЕНИЕ РАЗМЕРА ИЗОБРАЖЕНИЯ
# img = cv2.imread('images/ozero.jpg')
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# cv2.imshow('KARTINKA', img)
#
# cv2.waitKey(0)
#
#
# # ОБРЕЗАТЬ ИЗОБРАЖЕНИЕ
# img = cv2.imread('images/ozero.jpg')
# img = cv2.resize(img, (500, 500))
# cv2.imshow('KARTINKA', img[0:100, 0:150])
#
# cv2.waitKey(0)

# СОЗДАЕМ МАТРИЦУ
kernel = np.ones((5, 5), np.uint8)

# ИЗМЕНЕНИЕ ХАРАКТЕРИСТИК ИЗОБРАЖЕНИЯ
img = cv2.imread('images/ozero.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) # половина от размера
img = cv2.GaussianBlur(img, (9, 9), 0) # размытие
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # ч/б оттенки
img = cv2.Canny(img, 100, 100) # бинарная (ч/б - 1,0)
img = cv2.dilate(img, kernel, iterations=1) # ширина точек (обводка)


img = cv2.erode(img, kernel, iterations=1)


cv2.imshow('KARTINKA', img)
cv2.waitKey(0)