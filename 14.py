#RECIZING AN IMAGE - SCALING AN IMAGE

import cv2
import numpy as np
img=cv2.imread('abc.jpg')
cv2.imshow('original',img)
cv2.waitKey(2000)

#SCALE DOWM THE IMAGE
img_sc=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('scaled down image',img_sc)
cv2.waitKey(0)
cv2.destroyAllWindows()

#scale up
img_sc1=cv2.resize(img,None,fx=2,fy=2)
cv2.imshow('scaled up image',img_sc1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#SCALING USING CUSTOMISATIONS
img_sc2=cv2.resize(img,(1000,400)) #1000 IS THE LENGTH AND 400 IS THE WIDTH
cv2.imshow('CUSTOM IMAGE',img_sc2)
cv2.waitKey(0)
cv2.destroyAllWindows()

