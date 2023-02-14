from PIL import Image, ImageDraw, ImageFont
import os

# Prompt user for path to image
image_path = input("Path to image: ")

# Extract date from file name
date_str = os.path.basename(image_path).split("_")[1]
date = f"{date_str[6:]}-{date_str[4:6]}-{date_str[:4]}"

# Open image and get dimensions
image = Image.open(image_path)
width, height = image.size

# Add date to top right corner of image
font = ImageFont.truetype("arial.ttf", size=40)
draw = ImageDraw.Draw(image)
text_width, text_height = draw.textsize(date, font=font)
draw.text((width - text_width, 0), date, font=font, fill=(255, 255, 255, 128))

# Rotate image back to original orientation
if width < height:
    image = image.rotate(90, expand=True)

# Save modified image in same directory as original image
directory = os.path.dirname(image_path)
filename = os.path.splitext(os.path.basename(image_path))[0] + "-modified.jpg"
save_path = os.path.join(directory, filename)
image.save(save_path)
