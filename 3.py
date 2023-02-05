#reading the information of the image
import cv2
img=cv2.imread('abc.jpg')
print(img.shape)

#(664, 1601, 3)
#664 is height of the image
#1601 is the width of the image
#3 is the depth/chanell number (RGB)
