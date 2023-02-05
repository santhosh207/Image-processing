#17. CLICK BUTTON PROJECT

import cv2
import numpy as np

#create a black image and a window
windowName='drawing'
cv2.namedWindow(windowName)
img=np.zeros((500,500,3))

#mouse callback function
#flags and params are not used at all but m we need to weite in mouse callback function
def circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #left button double click
        cv2.circle(img,(x,y),40,(0,255,0),-1) #source, center point, radius, colour, thickness

    if event == cv2.EVENT_RBUTTONDBLCLK:
         cv2.circle(img,(x,y),30,(255,255,255),-1)

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,255,255),-1)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)

cv2.setMouseCallback(windowName,circle) #function call

while(True):
    cv2.imshow(windowName,img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()

                    
    
