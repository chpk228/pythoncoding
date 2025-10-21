import cv2
import matplotlib.pyplot as plt

img = cv2.imread('input_image.jpg')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0].set_title("Original")
ax[0].axis('off')

ax[1].imshow(gray_image, cmap='gray')
ax[1].set_title("Grayscale")
ax[1].axis('off')

plt.show()

