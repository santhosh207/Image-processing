#8. all the 3 solid colours in one single image
import cv2
import numpy as np
img=np.zeros((300,300,3))
img[0:100,0:300]=0,255,0 #green
#      y,x
img[100:200,0:300]=0,0,255 #red
img[200:300,0:300]=255,0,0 #blue
cv2.imshow('primary colours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
