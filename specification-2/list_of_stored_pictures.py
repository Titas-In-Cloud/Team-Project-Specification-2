import os

storage_folder = ".\picture_storage_folder"

for picture in os.listdir(storage_folder):
    print(picture)
