# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 14:38:57 2018

@author: ecupl
"""

#实例：抓取图像，并截图，识别面孔并保存
import cv2,os
#import numpy as np
from PIL import Image
if not os.path.exists('face'):
    os.mkdir('face')
currpath = os.getcwd()

#cv2.namedWindow('frame')
cap=cv2.VideoCapture(0)     #调用摄像头
while (cap.isOpened()):     #验证是否打开
    ret,img = cap.read()    #截取图片
    if ret == True:
        cv2.imshow('frame',img)     #在平台上打开
        k = cv2.waitKey(10)         #自动等待10ms
        if k==ord('z') or k==ord('Z'):  #判断是否为按了Z
            cv2.imwrite("catch.jpg",img)
            break
cv2.waitKey(500)
#识别面孔
faceCascade = cv2.CascadeClassifier("D:\\python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
peopleface = faceCascade.detectMultiScale(img,scaleFactor=1.2,minNeighbors=3,minSize=(10,10),flags=cv2.CASCADE_SCALE_IMAGE)
cv2.rectangle(img,(10,img.shape[0]-30),(110,img.shape[0]),(0,0,0),-1)
cv2.putText(img,"there are {}".format(len(peopleface)),(10,img.shape[0]-12),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
face = Image.open('catch.jpg')

n=1
for x,y,w,h in peopleface:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    face1 = face.crop((x,y,x+w,y+h))
    face2 = face1.resize((100,100),Image.ANTIALIAS)
    face2.save('face\\face%d.jpg'%n)
    n+=1

cv2.imshow('frame',img)
cv2.imwrite("catchdetect.jpg",img)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()


