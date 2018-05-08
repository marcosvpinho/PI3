# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:27:07 2018

@author: Marcos
"""

#Retorna uma janela que move com um passo de tamanho arbitrário
#da esquerda para a direita até a borda, então volta para a borda esquerda
#com um passo para baixo. Repete até o fim da imagem.        
def sliding_window(image, stepSize, windowSize):
    for y in xrange(0, image.shape[0], stepSize):
        for x in xrange(0, image.shape[1], stepSize):
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])