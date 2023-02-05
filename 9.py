#rgb extractions
#red tinted image
import numpy as np
import cv2

img=cv2.imread('abc.jpg')
cv2.imshow('original image',img)
B,G,R=cv2.split(img)
zeros=np.zeros(img.shape[:2],dtype='uint8')
#'uint8' sets the values in the range of 0 to 255
#img(shpape) has three attributes (length,breadth,chanell no)
    #(:2) selects only length and breadth
#np.zeros means black colour
cv2.imshow('red tinted image',cv2.merge([zeros,zeros,R]))#red tinted
cv2.imshow('green tinted image',cv2.merge([zeros,G,zeros]))#green tinted
cv2.waitKey(0)
cv2.destroyAllWindows()
