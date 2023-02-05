#7.solid colours- red,blue,green
import numpy as np
import cv2
img=np.zeros((250,250,3))#black background
#img[:]will select the whole image
img[:]=0,0,255 #we assign the colour(B,G,R)
#green-0,255,0
#blue-255,0,0 we can also do colour mixing
cv2.imshow('red',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
