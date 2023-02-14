# Script that turns all the images .jpg and .png that are inside a folder into a PDF file, images ordered by name 

import io
import os
from PIL import Image
from PyPDF4 import PdfFileMerger

while True:
    # Prompt the user to enter the path to the folder with the images
    image_folder = input('Path to folder: ')
    
    # Check if the path exists
    if os.path.exists(image_folder):
        # Check if the path contains any image files
        image_filenames = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
        if image_filenames:
            break
        else:
            print("Path doesn't have any images. Please try again.")
    else:
        print("Invalid path. Please try again.")

# Create a list of image filenames, sorted by name
image_filenames = sorted(image_filenames)

# Extract the last component of the image_folder path as the output filename
output_filename = os.path.basename(image_folder) + '.pdf'

# Create the full output file path using os.path.join()
output_file_path = os.path.join(image_folder, output_filename)

# Check if the output file already exists and is a regular file
file_exists = os.path.isfile(output_file_path)

# Create a PDF file and open it in write binary mode in the same directory as the input images
pdf_file = open(output_file_path, 'wb')

# Create a PyPDF4 PdfFileMerger object
pdf_merger = PdfFileMerger()

# Loop through the image filenames
for image_filename in image_filenames:
    # Open the image file
    image_file = Image.open(os.path.join(image_folder, image_filename))

    # Create a binary stream or file object from the image
    with io.BytesIO() as pdf_bytes:
        image_file.convert('RGB').save(pdf_bytes, format='PDF')
        pdf_bytes.seek(0)

        # Add the PDF page to the PyPDF4 PdfFileMerger object
        pdf_merger.append(pdf_bytes)

# Write the PDF file to disk
pdf_merger.write(pdf_file)

# Close the PDF file
pdf_file.close()

# Print a message to the console to let the user know the file was created or updated
if file_exists:
    print(f'{output_filename} file updated')
else:
    print(f'{output_filename} file created')
