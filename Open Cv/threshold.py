import cv2 

image1 = cv2.imread('photo.png') 
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
ret, img2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) 

cv2.imshow('Threshold', img2)
cv2.waitKey(0)
cv2.imwrite("photo_threshold.png", img2)