import cv2
import numpy as np

img = cv2.imread('input_image.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

edges = cv2.Canny(blurred_img, 50, 150)

cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray_img)
cv2.imshow('Blurred Image', blurred_img)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
