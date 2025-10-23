from PIL import Image, ImageFilter

image = Image.open('input_image.jpg')
sharpened_image = image.filter(ImageFilter.SHARPEN)
sharpened_image.save('sharpened_image.jpg')
sharpened_image.show()

