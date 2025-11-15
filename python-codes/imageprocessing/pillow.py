from PIL import Image

img = Image.open("input.jpg")
resized = img.resize((400, 400))
rotated = img.rotate(45)
gray = img.convert("L")

resized.save("resized.jpg")
rotated.save("rotated.jpg")
gray.save("gray.jpg")

