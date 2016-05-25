import cv2

img = cv2.imread('../fig/lena512.jpg',1)

cv2.imshow('Lena', img)
cv2.waitKey(0)
cv2.destroyWindow('Lena')
