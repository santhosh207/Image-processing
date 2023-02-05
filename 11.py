#11. HSV FILTERS  (hue, saturation , value/luninisity)
import numpy as np
import cv2

img=cv2.imread('abc.jpg')
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv filter',img_hsv)

cv2.imshow('hue filter',img_hsv[:,:,0]) #HUE IMAGE
cv2.imshow('saturatin filter',img_hsv[:,:,1]) #SATURATION FILTER
cv2.imshow('value filter',img_hsv[:,:,2]) #VALUE FILTER

CV2.waitKey(0)
CV2.destroyAllWindows()


           
