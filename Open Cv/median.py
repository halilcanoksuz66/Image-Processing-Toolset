import cv2 
  
image = cv2.imread('photo_salt.png') 
median = cv2.medianBlur(image, 3)
cv2.imshow('Median', median)
cv2.imwrite("photo_median.png", median)
cv2.waitKey(0)