# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:26:26 2018

@author: Marcos
"""

import cv2
import numpy as np

datapath = "/path/to/CarData/TrainImages/"
SAMPLES = 400

def path(cls,i):
    return "%s/%s%d.pgm"% (datapath,cls,i+1)

#definindo função util para obter o flann matcher    
def get_flann_matcher():
    flann_params = dict(algorithm = 1, trees = 5)
    return cv2.FlannBasedMatcher(flann_params, {})

#retorna as caracteristicas do BOW
def get_bow_extractor(extract, flann):
    return cv2.BOWImgDescriptorExtractor(extract, flann)
    
#retorna as caracteristicas do SIFT detector
def get_extract_detect():
    return cv2.xfeatures2d.SIFT_create(),cv2.xfeatures2d.SIFT_create()

#retorna caracteristicas da imagem        
def extract_sift(fn, extractor, detector):
    im = cv2.imread(fn,0)
    return extractor.compute(im, detector.detect(im))[1]
    
def bow_features(img, extractor_bow, detector):
    return extractor_bow.compute(img, detector.detect(img))
    
def car_detector():
    pos, neg = "pos-", "neg-"
    detect, extract = get_extract_detect()
    matcher = get_flann_matcher()
    print "building BOWKMeansTrainer..."
    bow_kmeans_trainer = cv2.BOWKMeansTrainer(1000)
    extract_bow = cv2.BOWImgDescriptorExtractor(extract, flann)
    
    print "adding features to trainer"
    for i in range(SAMPLES):
        print i
        bow_kmeans_trainer.add(extract_sift(path(pos,i), extract,detect))
        bow_kmeans_trainer.add(extract_sift(path(neg,i), extract,detect))
        
    voc = bow_kmeans_trainer.cluster()
    extract_bow.setVocabulary( voc )
    traindata, trainlabels = [],[]
    print "adding to train data"
    for i in range(SAMPLES):
        print i
        traindata.extend(bow_features(cv2.imread(path(pos, i), 0),extract_bow, detect))
        trainlabels.append(1)
        traindata.extend(bow_features(cv2.imread(path(neg, i), 0),extract_bow, detect))
        trainlabels.append(-1)
        
    svm = cv2.ml.SVM_create()
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setGamma(0.5)
    svm.setC(30)
    svm.setKernel(cv2.ml.SVM_RBF)
    
    svm.train(np.array(traindata), cv2.ml.ROW_SAMPLE,np.array(trainlabels))
    return svm, extract_bow