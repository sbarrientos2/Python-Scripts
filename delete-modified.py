import os

# Prompt user for path to folder containing images
folder_path = input("Path to folder containing files: ")

# Get list of all files in folder
files = os.listdir(folder_path)

# Filter out files that contain the string "-modified"
modified_files = [file for file in files if "-modified" in file]

# Loop over modified files and delete them
for file in modified_files:
    # Create path to current file
    file_path = os.path.join(folder_path, file)
    
    # Delete file
    os.remove(file_path)
    
print("Modified files deleted successfully!")
