from PIL import Image
import os

# Prompt user for path to folder containing images
folder_path = input("Path to folder containing images: ")

# Get list of all files in folder
files = os.listdir(folder_path)

# Filter image files that contain the word "-modified"
image_files = [file for file in files if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") and "-modified" in file]

# Loop over image files and apply rotation
for file in image_files:
    # Create path to current image file
    image_path = os.path.join(folder_path, file)

    # Open image
    image = Image.open(image_path)

    # Rotate image 90 degrees to the right
    rotated_image = image.transpose(Image.ROTATE_270)

    # Overwrite original image with rotated image
    rotated_image.save(image_path)

print("Image rotation completed successfully!")
