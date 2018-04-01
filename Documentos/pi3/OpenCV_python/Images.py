# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

# para fechar as imagens aperte qualquer tecla!!!!

# criando duas imagens aleatorias nos espaços de cores grays e bgr 
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
bgrImage = flatNumpyArray.reshape(100, 400, 3)

cv2.imshow('teste1',grayImage)
cv2.imshow('teste2',bgrImage)



# abrindo uma imagem
image = cv2.imread('download.jpg',cv2.IMREAD_GRAYSCALE)
byteArray = bytearray(image)
cv2.imwrite('MyPic.png', image)


image2 = cv2.imread('download.jpg')

#modificando um pixel especifico
print image2.item(150,120,0)
image2.itemset((150,120,0),255)
print image2.item(150,120,0)

cv2.imshow('download',image2)
cv2.waitKey()
cv2.destroyAllWindows()