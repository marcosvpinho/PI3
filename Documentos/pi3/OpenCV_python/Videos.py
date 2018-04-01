# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:40:25 2018

@author: marcos
"""

import cv2

#'Click na imagem ou aperte alguma tecla para sair.'

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Stream')
cv2.setMouseCallback('Stream', onMouse)

fps = 30 # an assumption
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#'gravar em outro arquivo para não sobreescrever o video'
videoWriter = cv2.VideoWriter('gravado.avi', cv2.VideoWriter_fourcc('I','4','2','0'),fps, size)


success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('Stream', frame) 
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    
cv2.destroyWindow('Stream')
cameraCapture.release()