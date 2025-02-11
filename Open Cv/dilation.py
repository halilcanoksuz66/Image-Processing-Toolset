import cv2
import numpy as np

image = cv2.imread("photo_threshold.png")
kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imshow("Dilation", dilation)
cv2.imwrite("photo_dilation.png", dilation)
cv2.waitKey(0)