import cv2
import matplotlib.pyplot as plt

img = cv2.imread('input_image.jpg')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
edges = cv2.Canny(image_rgb, 100, 200)

plt.imshow(edges, cmap='gray')
plt.title('Edges')
plt.axis('off')
plt.show()

