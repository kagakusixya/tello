import socket
import time

import cv2

cascade_path="haarcascade_frontalface_default.xml"
color = (255, 255, 255)

tello_ip = '192.168.10.1'
tello_port = 8889

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = (tello_ip , tello_port)

s.sendto('command'.encode('utf-8'),tello_address)

s.sendto('streamon'.encode('utf-8'),tello_address)

s.sendto('takeoff'.encode('utf-8'),tello_address)

capture = cv2.VideoCapture('udp://localhost:11111')

i = 1

dx = int(960/2)
dy = int(720/2)

lang = 100
print(dx-lang)
while(True):
    i += 1
    ret, frame = capture.read()
    cv2.rectangle(frame,(dx-lang,dy-lang),(dx+lang,dy+lang),(255,0,0), thickness=2)
    if i%20 == 0:
        i = 1
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))
        if len(facerect) > 0:
            x = facerect[0][0] + (facerect[0][0] + facerect[0][2])
            y = facerect[0][1] + (facerect[0][1] + facerect[0][3])
            if x/2 < dx-lang :
                s.sendto('ccw 15'.encode('utf-8'),tello_address)
                print("hidari")
            elif x/2 > dx+lang :
                s.sendto('cw 15'.encode('utf-8'),tello_address)
                print("migi")
            else :
                print("x,ok!")
            if y/2 < dy-lang :
                s.sendto('up 30'.encode('utf-8'),tello_address)
                print("ue")
            elif y/2 > dy+lang :
                s.sendto('down 30'.encode('utf-8'),tello_address)
                print("sita")
            else :
                print("y,ok!")
            for rect in facerect:
                cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()
