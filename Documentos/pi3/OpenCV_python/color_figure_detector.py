# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:47:13 2018

@author: marcos
"""

import cv2 
import numpy as np

frame = cv2.imread('infrared.jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow("contours1", frame)

#convertendo frame BGR para HSV            
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#definindo o range da cor vermelho

lower_red = np.array([136,87,111],np.uint8)
upper_red = np.array([180,255,255],np.uint8)

#definindo o range da cor azul

lower_blue = np.array([99,115,150],np.uint8)
upper_blue = np.array([110,255,255],np.uint8)

#definindo o range da cor amarelo

lower_yellow = np.array([22,60,200],np.uint8)
upper_yellow = np.array([60,255,255],np.uint8)

red=cv2.inRange(hsv,lower_red,upper_red)
blue=cv2.inRange(hsv,lower_blue,upper_blue)
yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
    
  
#detectando a cor vermelha
(_,contours,hierarchy)=cv2.findContours(red,cv2.cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate (contours):
    area = cv2.contourArea(contour)
    if(area>300):
        x,y,w,h = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,"Vermelho",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))
        
        
(_,contours,hierarchy)=cv2.findContours(blue,cv2.cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate (contours):
    area = cv2.contourArea(contour)
    if(area>300):
        x,y,w,h = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,"Azul",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))
      
(_,contours,hierarchy)=cv2.findContours(yellow,cv2.cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for pic, contour in enumerate (contours):
    area = cv2.contourArea(contour)
    if(area>300):
        x,y,w,h = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(90,255,255),2)
        cv2.putText(frame,"Amarelo",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(90,255,255))       
        
cv2.imshow("detector",frame)
cv2.waitKey()
cv2.destroyAllWindows()