import cv2

image = cv2.imread("photo.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filtered_image = cv2.Laplacian(image_gray, cv2.CV_16S, ksize=5)
cv2.imshow('Laplacian', filtered_image)
cv2.waitKey(0)
cv2.imwrite("photo_laplacian.png", filtered_image)