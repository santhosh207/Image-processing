#4 grayscale image(black and white)
import cv2
img=cv2.imread('abc.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('normal image',img)
cv2.imshow('gray scale imag',gray)
cv2.imwrite('black_white.jpg',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
