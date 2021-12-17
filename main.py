import cv2

#загружаем изображение
img= cv2.imread('Images/img1.jpg')
img= cv2.resize(img, (1000, 600))

#преобразуем к серому изображению
grey= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Подключаем нейросеть
plate= cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

#Определяем координаты носерной рамки
plate_point= plate.detectMultiScale(img, scaleFactor=1.8, minNeighbors=3)

#print(plate_point)

#
for (x, y, w, h) in plate_point:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)


cv2.imshow('test1', img)
cv2.waitKey(0)
