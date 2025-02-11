import cv2
import numpy as np

img = cv2.imread("photo.png")

kernel = np.array([[0,-2,0],[-2,11,-2],[0,-2,0]]) / 3
sharpening = cv2.filter2D(img,-1,kernel)

cv2.imshow("Sharpened Image",sharpening)
cv2.imwrite("photo_sharpening.png", sharpening)
cv2.waitKey(0)