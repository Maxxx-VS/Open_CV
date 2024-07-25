import cv2
import numpy as np
import imutils
# import easyocr
from matplotlib import pyplot as plt

import cv2

img = cv2.imread("images/cars/car1.jpg")
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 150, 150)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)[:8]

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, )


plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.show()