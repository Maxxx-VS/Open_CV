import cv2

# РАБОТА С ИЗОБРАЖЕНИЯМИ
img = cv2.imread('images/ozero.jpg')
cv2.imshow('KARTINKA', img)

cv2.waitKey(0)

# РАБОТА С ВИДЕО
cap = cv2.VideoCapture('videos/sample.mp4')

while True:
    sucess, img = cap.read()
    cv2.imshow('KARTINKA', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# РАБОТА С WEB-КАМЕРОЙ
cap = cv2.VideoCapture(0)
cap.set(3, 300)
cap.set(4, 500)

while True:
    sucess, img = cap.read()
    cv2.imshow('KARTINKA', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

