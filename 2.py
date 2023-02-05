#2 create a duplicate image
import cv2
img=cv2.imread('abc.jpg')
cv2.imshow('output',img)
cv2.imwrite('santhu.png',img)

cv2.waitKey(3000)
cv2.destroyAllWindows()
