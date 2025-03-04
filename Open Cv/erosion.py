import cv2
import numpy as np

image = cv2.imread("photo_threshold.png")
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Erosion", erosion)
cv2.imwrite("photo_erosion.png", image)
cv2.waitKey(0)