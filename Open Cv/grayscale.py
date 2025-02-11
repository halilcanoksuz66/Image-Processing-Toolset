import cv2

I1 = cv2.imread('photo.png')
I2 = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',I2)
cv2.imwrite("photo_grayscale.png", I2)
cv2.waitKey(0)