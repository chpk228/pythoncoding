import cv2

img = cv2.imread("input.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("output.jpg", img)

