import cv2

img = cv2.imread("images/faces/faces3.jpg")
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow("Result", img)
cv2.waitKey(0)