#15. RECTANGLE

import cv2
import numpy as np

img=np.zeros((500,500,3))  #BLACK BACKGROUND

#cv2.rectangle(scr,staart point,end point, colour , thickness)
cv2.rectangle(img,(200,200),(400,400),(0,255,0),7)
cv2.imshow('RECTANGEL',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
