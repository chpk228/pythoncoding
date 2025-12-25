import cv2
image = cv2.imread("input_image.jpg")
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayscale_image.jpg", grayscale_image)

