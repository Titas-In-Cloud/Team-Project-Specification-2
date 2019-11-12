import os
from PIL import Image

""" 
Saves the image when the function is called

Parameters:
image (file): image file opened with Pillow library
image_name (string): image file name
    
"""
def image_save(image, image_name):
    image_storage_location_path = \
        input(" * Where would you like to save the modified picture? ")

    # creates path if the path does not exist in the directory
    if os.path.isdir(image_storage_location_path) == False:
        os.mkdir(image_storage_location_path)


    new_picture_name_question = input(" * Would you like to give a new name to the modified picture? ")

    # variable used to determine if input was right (False = Yes, True = No)
    error = True

    while error == True:
        if new_picture_name_question == "Yes" or new_picture_name_question == "yes":
            new_name = input(" * Please write new name here: ")
            image.save(image_storage_location_path + "\\" + new_name + ".jpeg")
            error = False

        elif new_picture_name_question == "No" or new_picture_name_question == 'no':
            image.save(image_storage_location_path + "\\" + image_name)
            error = False

        else:
            print("- Error! Wrong command. Please choose 'Yes' or 'No'.")
            new_picture_name_question = input(" * Would you like to give a new name to the modified picture? ")

    print("- Success! Image was saved.")
