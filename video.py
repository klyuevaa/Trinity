import cv2

cap= cv2.VideoCapture('Video/outfile.mp4')
cap.set(3, 50)
cap.set(4, 30)

while True:
    success, frame = cap.read()
    #_, frame = vs.read()
    (w, h, c) = frame.shape



#syntax: cv2.resize(img, (width, height))
    img = cv2.resize(frame,(800, 600))
    grey= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    plate= cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
    plate_point= plate.detectMultiScale(grey, scaleFactor=2.1, minNeighbors=2)
    for (x, y, w, h) in plate_point:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)
    cv2.imshow('test1', img)
    #Подключаем нейросеть
    

    #Определяем координаты носерной рамки
    

    #print(plate_point)

    #


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break