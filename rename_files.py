import os

# Script that is used to rename default photo names from IMG_20220905_180352.jpg to 20220905.jpg much cleaner name
def rename_files(path):
    for filename in os.listdir(path):
        if filename.startswith("IMG_"):
            new_filename = filename[4:12] + ".jpg"
            if os.path.exists(os.path.join(path, new_filename)):
                counter = 1
                while os.path.exists(os.path.join(path, new_filename[:-4] + f"_{counter}.jpg")):
                    counter += 1
                new_filename = new_filename[:-4] + f"_{counter}.jpg"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))

rename_files("path/to/folder")
