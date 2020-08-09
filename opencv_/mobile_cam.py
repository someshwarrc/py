import cv2 
import numpy as np
url = 'http://192.168.1.101:8080/video'
cap = cv2.VideoCapture(url)
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

while(True):
    ret, frame = cap.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            color = (255, 0, 0)
            stroke = 2
            end_x = x + w
            end_y = y + h
            cv2.rectangle(frame, (x,y), (end_x, end_y), color, stroke)
        cv2.imshow('frame',cv2.resize(frame, (600,400)))

    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()