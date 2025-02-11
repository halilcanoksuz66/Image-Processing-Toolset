import cv2

image = cv2.imread("photo.png")
alpha = 1.5
beta = 10

new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
cv2.imshow("New photo", new_image)
cv2.waitKey(0)