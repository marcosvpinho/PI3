# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 18:52:03 2018

@author: marcos
"""

import cv2
import numpy as np

#Determine if a rectangle if fully contained in another rectangle
def is_inside(o, i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih

#Draw rectangles around detected people    
def draw_person(image, person):
    x, y, w, h = person
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(img,"Pessoa",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))

img = cv2.imread("pessoas.jpg")

hog = cv2.HOGDescriptor() #create a HOG descriptor
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) #Define the descriptor with defaultpeople detector

found, w = hog.detectMultiScale(img)# This Detection returns an array of rectangles
found_filtered = []

for ri, r in enumerate(found):
    for qi, q in enumerate(found):
        if ri != qi and is_inside(r, q):
            break
        else:
            found_filtered.append(r)
            
for person in found_filtered:
    draw_person(img, person)

cv2.imshow("detector de pessoa", img)
cv2.waitKey(0)
cv2.destroyAllWindows()