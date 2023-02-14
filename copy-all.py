# Script that prompts the user for a path to folder and copies everything inside this folder inside the other path given by user

import os
import shutil

# Prompt the user to enter the path of the folder to copy from
src_folder = input("Enter the path of the folder to copy: ")

# Check if the folder exists and is a directory
if not os.path.isdir(src_folder):
    print(f"Error: {src_folder} is not a valid directory.")
    exit()

# Prompt the user to enter the path of the folder to copy to
dst_folder = input("Enter the path of the folder to copy to: ")

# Check if the folder exists and is a directory
if not os.path.isdir(dst_folder):
    print(f"Error: {dst_folder} is not a valid directory.")
    exit()

# Copy the contents of the source folder to the destination folder
for item in os.listdir(src_folder):
    src_path = os.path.join(src_folder, item)
    dst_path = os.path.join(dst_folder, item)
    if os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path)
    else:
        shutil.copy2(src_path, dst_path)

print("Copy complete.")
