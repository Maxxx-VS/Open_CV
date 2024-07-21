import cv2
import numpy as np

img = cv2.imread("images/ozero.jpg")

# img = cv2.flip(img, 1) # отзеркаливание (1, 0, -1)


def rotate(img_param, angle):
    h, w = img_param.shape[:2]
    point = (w // 2, h // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (w, h))

# img = rotate(img, 90)

def transform(img_parm, x , y):
    mat = np.float32([[1, 0, x], [0, 1 , y]])
    return cv2.warpAffine(img_parm, mat, (img_parm.shape[1], img_parm.shape[0]))

img = transform(img, 30, 200)


cv2.imshow('Result' , img)
cv2.waitKey(0)