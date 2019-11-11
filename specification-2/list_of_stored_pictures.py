import os

# folder path where the pictures are temporarily stored for modification
storage_folder = ".\picture_storage_folder"

# prints the name of each chosen picture file which are stored in the storage folder
for picture in os.listdir(storage_folder):
    print(picture)
