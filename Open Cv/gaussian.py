import cv2 
  
image = cv2.imread('photo.png')
Gaussian = cv2.GaussianBlur(image, (7, 7), 0) 
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.imwrite("photo_gaussian.png", Gaussian)
cv2.waitKey(0)