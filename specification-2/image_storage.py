import os
from PIL import Image

# folder path where the pictures will be temporarily stored for modification
storage_folder = ".\picture_storage_folder"

# creates storage folder if it does not exist
if os.path.isdir(storage_folder) == False:
    os.mkdir(storage_folder)

images_directory_for_storage = input(" * What picture/s would you like "
                                     "to store for modification: ")

if os.path.isdir(images_directory_for_storage) == True:
    # variable used to determine if input was right (False = Yes, True = No)
    error = True

    chosen_pictures = 0

    # loop will stop only when the person inputs the right answer ('Yes' or 'No')
    while error == True:
        storage_action_choice = input(" * Do you want to choose which pictures you want "
                                      "to store for modification from this folder? ")

        # function which lets person choose what pictures he wants to store for modification
        if storage_action_choice == "Yes" or storage_action_choice == "yes":
            error = False

            # empties the storage folder
            for file in os.listdir(storage_folder):
                os.remove(storage_folder + "\\" + file)

            # reads all the files from chosen directory and asks if the person wants
            # to store each of it for modification
            for picture in os.listdir(images_directory_for_storage):
                # picks only files and skips directories(folders)
                if os.path.isfile(images_directory_for_storage + "\\" + picture):
                    image = Image.open(images_directory_for_storage + "\\" + picture)

                    # variable used to determine if input was right (False = Yes, True = No)
                    loop_run = True

                    while loop_run == True:
                        file_choice_answer = input(" * Do you want to store " + picture + "? ")
                        if file_choice_answer == "Yes" or file_choice_answer == "yes":
                            image.save(storage_folder + "\\" + picture)
                            chosen_pictures += 1
                            loop_run = False

                        elif file_choice_answer == "No" or file_choice_answer == "no":
                            loop_run = False

                        else:
                            print("- Error! Please choose 'Yes' or 'No'.")

        # function which stores all the pictures for modification from the chosen directory
        if storage_action_choice == "No" or storage_action_choice == "no":
            error = False

            # empties the storage folder
            for file in os.listdir(storage_folder):
                os.remove(storage_folder + "\\" + file)

            # reads all the files from the chosen directory and stores all the
            # files for modification
            for picture in os.listdir(images_directory_for_storage):
                # picks only files, stores them into the temporary storage folder
                # and skips directories(folders)
                if os.path.isfile(images_directory_for_storage + "\\" + picture):
                    image = Image.open(images_directory_for_storage + "\\" + picture)
                    image.save(storage_folder + "\\" + picture)

        if error == True:
            print("- Error! Please choose 'Yes' or 'No'")

    if storage_action_choice == "Yes" or storage_action_choice == "yes" and chosen_pictures != 0:
        print("- Success! Your chosen pictures from the folder were stored successfully.")

    elif storage_action_choice == "No" or storage_action_choice == "no":
        print("- Success! All pictures from the folder were stored successfully.")

    elif storage_action_choice == "Yes" or storage_action_choice == "yes" and chosen_pictures == 0:
        print("- Error! None of the pictures in the directory were selected.")

elif os.path.isfile(images_directory_for_storage) == True:
    # empties the storage folder
    for file in os.listdir(storage_folder):
        os.remove(storage_folder + "\\" + file)

    # splits the file path into file name and the rest of the directory path
    file_path, file_name = os.path.split(images_directory_for_storage)
    image = Image.open(images_directory_for_storage)

    # stores chosen picture to the temporary storage folder
    image.save(storage_folder + "\\" + file_name)
    print("- Success! Picture was scanned successfully.")

else:
    print("- Error! File or folder does not exist.")
