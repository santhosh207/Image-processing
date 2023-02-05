#12. EDGE DETECTION - 3 MAIN TYPES
#1.SOBEL 2.LAPLACIAN 3.CANNY
#SOBEL TERCHNIQUE (take only soduku image)

import cv2
img=cv2.imread('su.png',0) #0 is for gray scale image
sobel_x=cv2.Sobel(img,cv2.CV_8U,dx=1,dy=0,ksize=-1)
#cv_8U - unsigned 8 bit/pixel
#kernel - will define the size of convolution
sobel_y=cv2.Sobel(img,cv2.CV_8U,dx=0,dy=1,ksize=-1)
sobel_f = cv2.bitwise_or(sobel_x,sobel_y) #convolution happens (it means bitwise or)

cv2.imshow('sobel x image',sobel_x)


cv2.imshow('sobel y image',sobel_y)
cv2.imshow('sobel image',sobel_f)
cv2.waitKey(0)
cv2.destroyAllWindows()


