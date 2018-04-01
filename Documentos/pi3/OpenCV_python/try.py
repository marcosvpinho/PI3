# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 23:22:27 2018

@author: marcos
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,0,0])
    upper_red = np.array([180,255,255])


    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    blurKsize = 5
    frame = cv2.medianBlur(frame, blurKsize)
    ret, thresh = cv2.threshold(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)
    
    image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (255, 0, 0), 1)
        
    cv2.imshow('mask',frame)    
    

    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
            break
        
cv2.destroyAllWindows()
cap.release()        
       
    