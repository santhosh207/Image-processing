#16. CIRCLE

import cv2
import numpy as np

img=np.zeros((500,500,3)) #black

#cv2.circle(source, center position , radius, colout, thickness)
cv2.circle(img,(200,100),100,(0,0,255),5)
cv2.imshow('CIRCLE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
