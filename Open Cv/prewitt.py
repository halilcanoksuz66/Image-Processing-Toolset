import cv2
import numpy as np

img = cv2.imread("photo.png")

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewittx = cv2.filter2D(img,-1,kernelx)
prewitty = cv2.filter2D(img,-1,kernely)

cv2.imshow("prewittx.png",prewittx)
cv2.imshow("prewitty.png",prewitty)
cv2.imwrite("photo_prewitt.png", prewittx)
cv2.waitKey(0)