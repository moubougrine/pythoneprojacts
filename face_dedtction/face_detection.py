import cv2

face = cv2.CascadeClassifier('cascades\\fire.xml')
camera = cv2.VideoCapture(0)
while True:
    rete,fram = camera.read()
    gray=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    detection = face.detectMultiScale(gray,1.5,5,minSize=(100,100))
    for (x,y,h,w) in detection :
        cv2.rectangle(fram,(x+y),(x+y+h+w),(0,255,0),2)

    
