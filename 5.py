#5 binary image conversion
import cv2
img=cv2.imread('abc.jpg',0)#0 is added to obtain gray scale image
cv2.imshow('gray scale image',img)
cv2.waitKey(2000)
ret,binary=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#cv2.threshold(src,thresh value,max value,type of conversion
cv2.imshow('binary image',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
