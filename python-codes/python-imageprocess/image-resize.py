from PIL import Image

filename = "input_image.jpg"
with Image.open(filename) as img:
    resized_img = img.resize((200, 200), Image.Resampling.BILINEAR)
    resized_img.save("resized_image.jpg")
    resized_img.show()

