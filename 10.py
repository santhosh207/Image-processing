#10. creating a ckess board
import numpy as np
import cv2

img = np.zeros((300,300,3))#a black image of 200*200 poxels black image is formed
img[0:100,0:100] = 255,255,255 #white
img[100:200,100:200] = 255,255,255
img[100:200,100:200] = 255,255,255


img[0:100,200:300] = 255,255,255
img[200:300,200:300] = 255,255,255
img[200:300,0:100] = 255,255,255


cv2.imshow('chess board',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#8*8 chess board
import numpy as np
import cv2
row=int (input('please enter the row number'))
column=int (input('please enter the column number'))
while True:
 chess=np.zeros((row,column),dtype=np.uint8)
 for r in range(0,row,100):
 for c in range(0,column,100):
 chess[r:r+49,c:c+49]=255
 chess[r+49:r+(2*49),c+49:c+(2*49)]=255
 cv2.imshow('chess',chess)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
