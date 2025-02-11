import cv2

image = cv2.imread("photo.png")
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotation", rotated_image)
cv2.imwrite("photo_rotate.png", rotated_image)
cv2.waitKey(0)