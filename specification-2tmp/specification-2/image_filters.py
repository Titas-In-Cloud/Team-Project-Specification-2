import os
from PIL import Image
from PIL import ImageFilter

import image_save

# folder path where the pictures are temporarily stored for modification
storage_folder = ".\picture_storage_folder"

print("Please input 'Help' to get a list of available filters and modifications. ")

command = "start the loop"


for picture in os.listdir(storage_folder):
    image = Image.open(storage_folder + "\\" + picture)
    print(picture + " was picked for modification.")
    while command != "End":
        command = input("What would you like to do? ")

        # prints a list with available commands
        if command == "Help" or command == "help":
            print("Haha! It is not done yet.")

        # shows modified picture
        elif command == "Show" or command == "show":
            image.show()

        # blurs picture
        elif command == "Blur" or command == "blur":
            image = image.filter(ImageFilter.BLUR)
            picture_with_last_modification_was_saved = False

        # contours picture
        elif command == "Contour" or command == "contour":
            image = image.filter(ImageFilter.CONTOUR)
            picture_with_last_modification_was_saved = False

        # emboss picture
        elif command == "Emboss" or command == "emboss":
            image = image.filter(ImageFilter.EMBOSS)
            picture_with_last_modification_was_saved = False

        # enhances pictures
        elif command == "Enhance" or command == "enhance":
            edge_enhance_picture_answer = input("Do you want to enhance picture a lot? ")
            if edge_enhance_picture_answer == "Yes" or edge_enhance_picture_answer == "yes":
                image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
                picture_with_last_modification_was_saved = False
            elif edge_enhance_picture_answer == "No" or edge_enhance_picture_answer == "no":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
                picture_with_last_modification_was_saved = False

        # rotates the picture some amount of degrees
        elif command == "Rotate" or command == "rotate":
            rotation_degrees = int(input("How much degrees you would like to rotate the picture? "))
            image = image.rotate(rotation_degrees)
            picture_with_last_modification_was_saved = False

        # cancels all modifications done to the image
        elif command == "Cancel" or command == "cancel":
            image = Image.open(storage_folder + "\\" + picture)
            picture_with_last_modification_was_saved = True

        # saves modified picture
        elif command == "Save" or command == "save":
            # splits the file path into file name and the rest of the directory path
            file_path, file_name = os.path.split(storage_folder + "\\" + picture)
            # calls save function from image_save.py file
            image_save.image_save(image, file_name)
            picture_with_last_modification_was_saved = True

        elif command == "End" or command == "end":
            if picture_with_last_modification_was_saved == False:
                save_confirmation = input("Do you want to end modification "
                                          "process without saving the picture "
                                          "with last adjustment? ")

                if save_confirmation == "Yes" or save_confirmation == "yes":
                    break

                if save_confirmation == "No" or save_confirmation == "no":
                    # splits the file path into file name and the rest of the directory path
                    file_path, file_name = os.path.split(storage_folder + "\\" + picture)
                    # calls save function from image_save.py file
                    image_save.image_save(image, file_name)
                    break

            else:
                break

        else:
            print("Error! Wrong command. Please input 'Help' to get a list of "
                  "available filters and modifications.")
