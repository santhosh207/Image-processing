#13. LAPLACIANS AND CANNY
import cv2
img=cv2.imread('abc.jpg',0) #gray scale
lap=cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('laplacian',lap)

canny=cv2.Canny(img,90,200) #thresh and max values
cv2.imshow('canny',canny)


cv2.waitKey(0)
cv2.destroyAllWindows()
