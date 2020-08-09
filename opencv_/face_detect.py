import cv2
import numpy as np
import os 

base_dir = os.path.dirname(os.path.abspath("__FILE__"))
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    cap.open()

while(True):
    # capture fram-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    # converting our frame to gray as haar cascade works with only grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        color = (255, 0, 0)
        stroke = 2
        end_x = x + w
        end_y = y + h
        cv2.rectangle(frame, (x,y), (end_x, end_y), color, stroke)

    # Display the color frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # wait for 'q' to exit
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()