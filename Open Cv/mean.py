import cv2 
  
image = cv2.imread('photo.png') 
average = cv2.blur(image, (3,3))
cv2.imshow('Average', average)
cv2.imwrite("photo_average.png", average)
cv2.waitKey(0)