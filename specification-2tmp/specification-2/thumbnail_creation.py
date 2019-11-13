import os
from PIL import Image

# folder path where the pictures are temporarily stored for modification
storage_folder = ".\picture_storage_folder"

thumbnail_dimensions = input("What size thumbnail would you like to create? ")

thumbnail_size = (int(thumbnail_dimensions), int(thumbnail_dimensions))

thumbnail_storage_location_path = \
        input("Where would you like to save created thumbnail/s? ")

# variable used to determine if the person chose one or multiple pictures
picture_amount_in_the_folder = 0

# creates path if the path does not exist in the directory
if os.path.isdir(thumbnail_storage_location_path) == False:
    os.mkdir(thumbnail_storage_location_path)

for picture in os.listdir(storage_folder):
    # splits the file path into file name and the rest of the directory path
    image_name, image_extension = os.path.splitext(picture)
    image = Image.open(storage_folder + "\\" + picture)
    # converts picture to chosen size thumbnail
    image.thumbnail(thumbnail_size)
    image_extension = ".jpeg"
    # saves created thumbnail to chosen directory
    image.save(thumbnail_storage_location_path + "\\" + "SIZE" + thumbnail_dimensions \
               + "_" + image_name + "_THUMBNAIL" + image_extension)
    picture_amount_in_the_folder += 1

if picture_amount_in_the_folder == 1:
    print("Success! Picture was successfully saved and converted to JPEG thumbnail")

else:
    print("Success! Pictures were successfully saved and converted to JPEG thumbnails")
