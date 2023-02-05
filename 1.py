#read an image

import cv2
img=cv2.imread('abc.jpg')
cv2.imshow('image',img)
cv2.waitKey(3000)#here the number is for milliseconds and give zero if you want image forever
cv2.destroyAllWindows()
