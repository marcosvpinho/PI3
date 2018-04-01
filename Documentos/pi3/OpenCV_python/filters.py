# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:20:57 2018

@author: marcos
"""

import cv2
import numpy
import utils
src = cv2.imread("download.jpg")
dst = cv2.imread("download.jpg")
dst1= dst

kernel = numpy.array([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]])

cv2.filter2D(src, -1, kernel, dst1)

cv2.imshow("3x1", dst) 
cv2.imshow("3x3", dst1)  
blurKsize = 7
edgeKsize = 5
    
if blurKsize >= 3:
    blurredSrc = cv2.medianBlur(src, blurKsize) #passando pelo filtro de desfoque
    graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY) #passando a imagem para gray scale
else:
    graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize = edgeKsize) #aplicando o filtro de detecção de borda
normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc) # invertendo para obter bordas pretas em um fundo branco
channels = cv2.split(src)
    
for channel in channels:
    channel[:] = channel * normalizedInverseAlpha
cv2.merge(channels, dst)
    
cv2.imshow("3x2", dst)  
cv2.waitKey()
cv2.destroyAllWindows()


class VConvolutionFilter(object):
    """A filter that applies a convolution to V (or all of BGR)."""
    def __init__(self, kernel):
        self._kernel = kernel
    def apply(self, src, dst):
        """Apply the filter with a BGR or gray source/destination."""
        cv2.filter2D(src, -1, self._kernel, dst)

class SharpenFilter(VConvolutionFilter):
    """A sharpen filter with a 1-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)
        
class FindEdgesFilter(VConvolutionFilter):
    """An edge-finding filter with a 1-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)
        
class BlurFilter(VConvolutionFilter):
    """A blur filter with a 2-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)
        
class EmbossFilter(VConvolutionFilter):
    """An emboss filter with a 1-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[-2, -1, 0],
                              [-1, 1, 1],
                              [ 0, 1, 2]])
        VConvolutionFilter.__init__(self, kernel)
        
        
        






#strokeEdges(img, dst, blurKsize = 7, edgeKsize = 5)
