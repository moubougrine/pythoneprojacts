import cv2

image = cv2.imread('img.jpg')
new_size = cv2.resize(image,(300,200))
cv2.imshow('moughit',new_size)
cv2.waitKey(0)