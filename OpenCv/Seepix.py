import cv2

image= cv2.imread('img.jpg')
pix = image.size
dimension=image.shape
print("Number of pix : ",pix)
print("Number of dimensions : ",dimension)
