import cv2

img = cv2.imread("photo.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

edgesx = cv2.Sobel(img, -1, dx=1, dy=0, ksize=1)
edgesy = cv2.Sobel(img, -1, dx=0, dy=1, ksize=1)
edges = edgesx + edgesy

cv2.imshow('sobel', edges)
cv2.imwrite("photo_sobel.png", edges)
cv2.waitKey(0)