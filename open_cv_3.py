import cv2
import numpy as np

# создание матрицы заполненные "0"
photo = np.zeros((450, 450, 3), dtype='uint8')

# RGB - standart
# BGR - OpenCV


# отображение квадрата на photo
# photo[10:150, 200:280] = 119, 201, 105


# создание пустого каодрата (рамка)
cv2.rectangle(photo, (20, 20), (50, 70), (119, 201, 10), thickness=3)


# создание линии
cv2.line(photo, (20, 10), (100, 10), (119, 201, 10), thickness=3)
cv2.line(photo, (10, photo.shape[0] // 2), (150, photo.shape[1] // 2), (10, 200, 100), thickness=3)


# создание круга
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (100, 50, 30), thickness=cv2.FILLED)


# вывод текста
cv2.putText(photo, 'Hello!', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0), thickness=2)




cv2.imshow('Photo', photo)
cv2.waitKey(0)