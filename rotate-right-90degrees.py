from PIL import Image
import os

# Prompt user for path to image
image_path = input("Path to image: ")

# Open image
image = Image.open(image_path)

# Rotate image 90 degrees to the right
rotated_image = image.transpose(Image.ROTATE_270)

# Overwrite original image with rotated image
rotated_image.save(image_path)

print("Image rotated and saved successfully!")
