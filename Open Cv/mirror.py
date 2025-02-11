import cv2

image = cv2.imread("photo.png")
mirrored_imageX = cv2.flip(image, 1)
mirrored_imageY = cv2.flip(image, 0)
cv2.imshow('MirrorX', mirrored_imageX)
cv2.imshow('MirrorY', mirrored_imageY)
cv2.imwrite("photo_mirrorX.png", mirrored_imageX)
cv2.imwrite("photo_mirrorY.png", mirrored_imageY)
cv2.waitKey(0)