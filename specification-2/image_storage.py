import os
from PIL import Image

# folder path where the pictures will be temporarily stored for modification
storage_folder = ".\picture_storage_folder"

# creates storage folder if it does not exist
if os.path.isdir(storage_folder) == False:
    os.mkdir(storage_folder)

images_directory_for_storage = input("What picture/s would you like "
                                     "to store for modification: ")

if os.path.isdir(images_directory_for_storage) == True:
    # used only as a temporary variable to define if the loop should run
    loop_operation_variable = "run"

    # loop will stop only when the person chooses the right answer ('Yes' or 'No')
    while loop_operation_variable == "run":
        storage_action_choice = input("Do you want to choose which pictures you want "
                                      "to store for modification from this folder? ")

        # function which lets person choose what pictures he wants to store for modification
        if storage_action_choice == "Yes" or storage_action_choice == "yes":
            loop_operation_variable = "stop"

            # deletes all the files in storage folder
            for file in os.listdir(storage_folder):
                os.remove(storage_folder + "\\" + file)

            # reads all the files from chosen directory and asks if the person wants
            # to store each of it for modification
            for picture in os.listdir(images_directory_for_storage):
                if os.path.isfile(images_directory_for_storage + "\\" + picture):
                    file_choice_answer = input("Do you want to store " + picture + "? ")
                    image = Image.open(images_directory_for_storage + "\\" + picture)

                    if file_choice_answer == "Yes" or file_choice_answer == "yes":
                        image.save(storage_folder + "\\" + picture)

        # function which stores all the pictures for modification from the chosen directory
        if storage_action_choice == "No" or storage_action_choice == "no":
            loop_operation_variable = "stop"

            # deletes all the files in temporary storage folder
            for file in os.listdir(storage_folder):
                os.remove(storage_folder + "\\" + file)

            # reads all the files from the chosen directory and stores all the
            # files for modification
            for picture in os.listdir(images_directory_for_storage):
                if os.path.isfile(images_directory_for_storage + "\\" + picture):
                    image = Image.open(images_directory_for_storage + "\\" + picture)
                    image.save(storage_folder + "\\" + picture)

        if loop_operation_variable == "run":
            print("Error! Wrong answer. Please choose 'Yes' or 'No'")

    loop_run = True

    while loop_run == True:
        if storage_action_choice == "Yes" or storage_action_choice == "yes":
            print("Success! Your chosen pictures from the folder were stored successfully.")
            loop_run = False

        elif storage_action_choice == "No" or storage_action_choice == "no":
            print("Success! All pictures from the folder were stored successfully.")
            loop_run = False

        else:
            "Error! Please choose 'Yes' or 'No'."

elif os.path.isfile(images_directory_for_storage) == True:
    # deletes all the files in storage folder
    for file in os.listdir(storage_folder):
        os.remove(storage_folder + "\\" + file)

    # splits the file path into file name and the rest of the directory path
    file_path, file_name = os.path.split(images_directory_for_storage)
    image = Image.open(images_directory_for_storage)
    # stores chosen picture to the temporary folder
    image.save(storage_folder + "\\" + file_name)
    print("Success! Picture was scanned successfully.")

else:
    print("Error! File or folder does not exist.")
