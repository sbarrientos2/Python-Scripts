import io
import os
from PIL import Image
from PyPDF4 import PdfFileMerger

# Prompt the user to enter the path to the folder with the images
image_folder = input('Path to folder: ')

# Create a list of image filenames, sorted by name
image_filenames = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')])

# Create a PDF file and open it in write binary mode in the same directory as the input images
pdf_file = open(os.path.join(image_folder, 'output.pdf'), 'wb')

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