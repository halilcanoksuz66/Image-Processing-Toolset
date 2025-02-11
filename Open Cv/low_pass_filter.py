import cv2
import numpy as np

image = cv2.imread("photo.png")
kernel = np.array(np.ones((5,5)))
kernel /= 25

new_image = cv2.filter2D(image, -1, kernel)
cv2.imshow("Low Pass Filter", new_image)
cv2.imwrite("photo_lps.png", new_image)
cv2.waitKey(0)