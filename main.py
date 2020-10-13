import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
# Cascades 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#Log 
log.basicConfig(filename='webcam.log',level=log.INFO)
anterior = 0
#Video out Things
is_record = 0 # If true records the video and saves it to a file.
if is_record == 1:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#Web cam
video_capture = cv2.VideoCapture(0)

while True:
    if not video_capture.isOpened(): #Checks if camera was opened
        print('Unable to load camera.')
        sleep(5)
        pass

    ret, frame = video_capture.read() # Capture frame-by-frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Creating gray frame

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
    )

    # Face Drawings
    for (x, y, w, h) in faces:
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (252,74,3), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.2,20)
        smiles = smile_cascade.detectMultiScale(roi_gray,1.8,15)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(252, 198, 3),2)
        for (ex,ey,ew,eh) in smiles:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0, 255, 0),2)
            
    if anterior != len(faces): # If face spotted: logs
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

    cv2.imshow('Video', frame) # Display the resulting frame

    if cv2.waitKey(1) & 0xFF == ord('q'): #Use to quit program
        break

    cv2.imshow('Video', frame) # Display the resulting frame
    
    if is_record == 1:
        out.write(frame)    

if is_record == 1: 
    out.release()

video_capture.release()
cv2.destroyAllWindows()


