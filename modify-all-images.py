from PIL import Image, ImageDraw, ImageFont
import os

# Prompt user for path to folder containing images
folder_path = input("Path to folder containing images: ")

# Create "modified" subfolder in original folder
modified_folder_path = os.path.join(folder_path, "modified")
if not os.path.exists(modified_folder_path):
    os.makedirs(modified_folder_path)

# Get list of all files in folder
files = os.listdir(folder_path)

# Filter out non-image files
image_files = [file for file in files if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")]

# Loop over image files and apply image modification
for file in image_files:
    # Create path to current image file
    image_path = os.path.join(folder_path, file)
    
    # Extract date from file name
    date_str = os.path.basename(image_path).split("_")[1]
    date = f"{date_str[6:]}-{date_str[4:6]}-{date_str[:4]}"
    
    # Open image and get dimensions
    image = Image.open(image_path)
    width, height = image.size
    
    # Add date to top right corner of image
    font = ImageFont.truetype("arial.ttf", size=180)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(date, font=font)
    draw.text((width - text_width, 0), date, font=font, fill=(255, 255, 255, 128))
    
    # Rotate image back to original orientation
    if width < height:
        image = image.rotate(90, expand=True)
    
    # Save modified image in "modified" subfolder
    filename = os.path.splitext(os.path.basename(image_path))[0] + "-modified.jpg"
    save_path = os.path.join(modified_folder_path, filename)
    image.save(save_path)
    
print("Image modifications completed successfully!")
