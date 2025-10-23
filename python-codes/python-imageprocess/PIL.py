from PIL import Image
import numpy as np

def process_image(image_path, output_path):
    img = Image.open(image_path)
    
    img_array = np.array(img)
    
    gray_array = (0.2989 * img_array[:, :, 0] + 0.5870 * img_array[:, :, 1] + 0.1140 * img_array[:, :, 2]).astype(np.uint8)
    
    gray_img = Image.fromarray(gray_array)
    
    resized_img = gray_img.resize((200, 200))
    
    rotated_img = resized_img.rotate(45)
    
    rotated_img.save(output_path)

if __name__ == "__main__":
    input_image = "example.jpg"
    output_image = "processed_example.jpg"
    
    # Create a dummy image for demonstration if it doesn't exist
    try:
        Image.open(input_image)
    except FileNotFoundError:
        dummy_img = Image.new('RGB', (400, 300), color = 'red')
        dummy_img.save(input_image)

    process_image(input_image, output_image)
