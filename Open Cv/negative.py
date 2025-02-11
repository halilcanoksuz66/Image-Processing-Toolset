import cv2 

img = cv2.imread('photo.png')
height, width, _ = img.shape

for i in range(0, height - 1): 
	for j in range(0, width - 1): 
		pixel = img[i, j] 
		
		pixel[0] = 255 - pixel[0]
		pixel[1] = 255 - pixel[1]
		pixel[2] = 255 - pixel[2]
		
		img[i, j] = pixel 

cv2.imshow('Negative', img)
cv2.waitKey(0)
cv2.imwrite("photo_negative.png", img)