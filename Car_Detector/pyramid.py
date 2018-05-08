# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:10:10 2018

@author: Marcos
"""

import cv2
import numpy as np

#Redimenciona a imagem em um fator especifico.
def resize(img, scaleFactor):
    return cv2.resize(img, (int(img.shape[1] * (1 / scaleFactor)),
        int(img.shape[0] * (1 / scaleFactor))),
            interpolation=cv2.INTER_AREA)
            
#Pega uma imagem e retorna uma versão redimensionada do mesmo até que as
#restrições mínimas de largura e altura sejam atingidas      
def pyramid(image, scale=1.5, minSize=(200, 80)):
    yield image

    while True:
        image = resize(image, scale)
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
    
        yield image
        
        
        
            