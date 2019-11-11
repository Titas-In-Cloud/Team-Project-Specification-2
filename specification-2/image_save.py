import os
from PIL import Image

def image_save(image, image_name):
    image_storage_location_path = \
        input("Where would you like to save the modified picture? ")

    # creates path if the path does not exist in the directory
    if os.path.isdir(image_storage_location_path) == False:
        os.mkdir(image_storage_location_path)

    loop_operation_variable = "run"
    new_picture_name_question = input("Would you like to give a new name to the modified picture? ")

    while loop_operation_variable == "run":
        if new_picture_name_question == "Yes" or new_picture_name_question == "yes":
            loop_operation_variable = "stop"
            new_name = input("Please write new name here: ")
            image.save(image_storage_location_path + "\\" + new_name + ".jpeg")

        elif new_picture_name_question == "No" or new_picture_name_question == 'no':
            loop_operation_variable = "stop"
            image.save(image_storage_location_path + "\\" + image_name)

        else:
            print("Error! Wrong command. Please choose 'Yes' or 'No'.")
            new_picture_name_question = input("Would you like to give a new name to the modified picture? ")
