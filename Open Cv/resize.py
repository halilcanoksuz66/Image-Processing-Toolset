import cv2

image = cv2.imread("photo.png")
resized = cv2.resize(image, (0,0), fx=0.2, fy=0.2)
cv2.imshow("Resized",resized)
cv2.imwrite("photo_resized.png", resized)
cv2.waitKey(0)