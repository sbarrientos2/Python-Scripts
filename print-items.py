# Print items from folder and the number of items

import os

while True:
    # Prompt the user to enter the path of the folder
    folder = input("Enter the path of the folder: ")

    # Check if the folder exists and is a directory
    if os.path.isdir(folder):
        break
    else:
        print(f"Error: {folder} is not a valid directory.")

files = os.listdir(folder)
file_count = 0

for file in files:
    file_count = file_count + 1
    print(file)

print("Number of items: " + str(file_count))
