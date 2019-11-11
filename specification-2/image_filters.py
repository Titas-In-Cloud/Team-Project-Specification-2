import os

from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import GaussianBlur
from PIL.ImageFilter import UnsharpMask

import image_save

# folder path where the pictures are temporarily stored for modification
storage_folder = ".\picture_storage_folder"

def custom_filter_saturation(value, quadrant_value):
    if value > 223:
        return 255
    elif value > 159:
        if quadrant_value != 1:
            return 255

        return 0

    elif value > 95:
        if quadrant_value == 0 or quadrant_value == 3:
            return 255

        return 0

    elif value > 32:
        if quadrant_value == 1:
            return 255

        return 0

    else:
        return 0

exit = False

print("Please input 'Help' to get a list of available filters and modifications. ")

for picture in os.listdir(storage_folder):
    if exit == True:
        break

    image = Image.open(storage_folder + "\\" + picture)

    image_size = os.path.getsize(storage_folder + "\\" + picture)

    picture_with_last_modification_was_saved = True
    error = False

    print(picture + " was picked for modification.")

    command = "start the loop"

    while command != "end the loop":
        # creates picture pixel map
        pixel_map = image.load()

        if error == False:
            command = input("How would you like to modify the picture? ")

        # prints a list with available commands
        if command == "Help" or command == "help":
            print("List of filters and modifications:")
            print(" * Show - shows the picture with applied filters \n"
                  " * Blur - applies blur filter to the picture \n"
                  " * Contour - applies contour filter to the picture \n"
                  " * Emboss - applies emboss filter to the picture \n"
                  " * Sharpen - applies sharpen filter to the picture \n"
                  " * Detail - applies detail filter to the picture \n"
                  " * Edges - applies edges filter to the picture \n"
                  " * Enhance - applies enhance filter to the picture \n"
                  " * Smooth - applies smooth filter to the picture \n"
                  " * Grayscale - applies custom greyscale filter \n"
                  " * Retro - applies custom retro filter \n"
                  " * Fried - applies custom filter \n"
                  " * Rotate - rotates the picture in inputed amount degrees \n"
                  " * Cancel - cancels all filters applied to the picture \n"
                  " * Save - saves the picture \n"
                  " * End - ends picture modification process \n"
                  " * Exit - exits filter program" )

        # shows modified picture
        elif command == "Show" or command == "show":
            image.show()

        # blurs picture
        elif command == "Blur" or command == "blur":
            blur_picture_answer = input("Do you want to make very blurred picture? ")
            if blur_picture_answer == "Yes" or blur_picture_answer == "yes":
                print("How much would you like to blur the image?")
                blur_radius_value = input("Choose a numeric value (bigger "
                                          "number = bigger blur effect): ")

                while blur_radius_value.isnumeric() == False:
                    print("Error! Please input numeric value.")
                    blur_radius_value = input("Choose a numeric value (bigger "
                                              "number = bigger blur effect): ")

                blur_radius_value = int(blur_radius_value)
                image = image.filter(GaussianBlur(radius = blur_radius_value))
                picture_with_last_modification_was_saved = False
                error = False

            elif blur_picture_answer == "No" or blur_picture_answer == "no":
                image = image.filter(ImageFilter.BLUR)
                picture_with_last_modification_was_saved = False
                error = False

            else:
                print("Error! Please choose 'Yes' or 'No'.")
                error = True

        # contours picture
        elif command == "Contour" or command == "contour":
            image = image.filter(ImageFilter.CONTOUR)
            picture_with_last_modification_was_saved = False

        # emboss picture
        elif command == "Emboss" or command == "emboss":
            image = image.filter(ImageFilter.EMBOSS)
            picture_with_last_modification_was_saved = False

        # sharpens picture
        elif command == "Sharpen" or command == "sharpen":
            sharp_picture_answer = input("Would you like to modify the sharpening aspects? ")
            if sharp_picture_answer == "Yes" or sharp_picture_answer == "yes":
                print("How detailed you would like to make the picture?")
                sharpen_radius_value = input("Input a numeric value(smaller "
                                             "number = more detailed picture): ")

                while sharpen_radius_value.isnumeric() == False:
                    sharpen_radius_value = input("Error! Please input a numeric value: ")

                print("How much contrast you would like to add to the picture edges?")
                sharpen_percentage_value = input("Input a numeric value(counted "
                                                 "in percentage, bigger percentage = "
                                                 "more contrast): ")

                while sharpen_percentage_value.isnumeric() == False:
                    sharpen_percentage_value = input("Error! Please input a numeric value: ")

                print("How much you would like to sharpen pronounced edges?")
                sharpen_threshold_value = input("Input a numeric value(smaller "
                                                "number = more sharp edges): ")

                while sharpen_threshold_value.isnumeric() == False:
                    sharpen_threshold_value = input("Error! Please input a numeric value: ")

                sharpen_radius_value = int(sharpen_radius_value)
                sharpen_percentage_value = int(sharpen_percentage_value)
                sharpen_threshold_value = int(sharpen_threshold_value)
                image = image.filter(UnsharpMask(radius = sharpen_radius_value,
                                                 percent = sharpen_percentage_value,
                                                 threshold = sharpen_threshold_value))
                picture_with_last_modification_was_saved = False
                error = False

            elif sharp_picture_answer == "No" or sharp_picture_answer == "no":
                image = image.filter(ImageFilter.SHARPEN)
                picture_with_last_modification_was_saved = False
                error = False

            else:
                print("Error! Please choose 'Yes' or 'No'.")
                error = True


        # details picture
        elif command == "Detail" or command == "detail":
            image = image.filter(ImageFilter.DETAIL)
            picture_with_last_modification_was_saved = False

        # edges picture
        elif command == "Edges" or command == "edges":
            image = image.filter(ImageFilter.FIND_EDGES)
            picture_with_last_modification_was_saved = False

        # enhances picture
        elif command == "Enhance" or command == "enhance":
            edge_enhance_picture_answer = input("Do you want to make very enhanced picture? ")
            if edge_enhance_picture_answer == "Yes" or edge_enhance_picture_answer == "yes":
                image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
                picture_with_last_modification_was_saved = False
                error = False

            elif edge_enhance_picture_answer == "No" or edge_enhance_picture_answer == "no":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
                picture_with_last_modification_was_saved = False
                error = False

            else:
                print("Error! Please choose 'Yes' or 'No'.")
                error = True

        # smoothens picture
        elif command == "Smooth" or command == "smooth":
            smooth_picture_answer = input("Do you want to make very smooth picture? ")
            if smooth_picture_answer == "Yes" or smooth_picture_answer == "yes":
                image = image.filter(ImageFilter.SMOOTH_MORE)
                picture_with_last_modification_was_saved = False
                error = False

            elif smooth_picture_answer == "No" or smooth_picture_answer == "no":
                image = image.filter(ImageFilter.SMOOTH)
                picture_with_last_modification_was_saved = False
                error = False

            else:
                print("Error! Please choose 'Yes' or 'No'.")
                error = True

        # applies custom greyscale filter to the picture
        elif command == "Grayscale" or command == "grayscale":
            for i in range(image.size[0]):
                for j in range(image.size[1]):
                    red, green, blue = pixel_map[i, j]
                    pixel_brightness = int(round(0.299 * red + 0.587 * green + 0.114 * blue))
                    pixel_map[i, j] = (pixel_brightness, pixel_brightness, pixel_brightness)

            picture_with_last_modification_was_saved = False

        # applies custom retro filter to the picture
        elif command == "Retro" or command == "retro":
            for i in range(image.size[0]):
                if i % 2 == 0:
                    for j in range(image.size[1]):
                        if j % 2 == 0:
                            coordinate = i, j
                            pixel = image.getpixel(coordinate)

                            # unpacks the pixel tuple
                            (red, green, blue) = pixel

                            r = [0]
                            g = [0]
                            b = [0]

                            # gets quadrant colors
                            r[0] = custom_filter_saturation(red, 0)
                            g[0] = custom_filter_saturation(green, 0)
                            b[0] = custom_filter_saturation(blue, 0)

                            # puts modified pixel values into the picture
                            pixel_map[i, j] = (r[0], g[0], b[0])

            picture_with_last_modification_was_saved = False

        # applies custom filter to the picture
        elif command == "Fried" or command == "fried":
            if image_size > 300000:
                print("Please, be patient, filter application to the bigger "
                      "file can take some time.")
            for i in range(image.size[0]):
                for j in range(image.size[1]):
                    # get pixels one by one around one of the pixels
                    coordinate = i, j
                    pixel_1 = image.getpixel(coordinate)
                    if image.size[0] != i + 1:
                        coordinate = i + 1, j
                        pixel_2 = image.getpixel(coordinate)

                    if image.size[1] != j + 1:
                        coordinate = i, j + 1
                        pixel_3 = image.getpixel(coordinate)

                    if image.size[0] != i + 1 and image.size[1] != j + 1:
                        coordinate = i + 1, j + 1
                        pixel_4 = image.getpixel(coordinate)

                    # unpacks tuple values
                    (px11, px12, px13) = pixel_1
                    (px21, px22, px23) = pixel_2
                    (px31, px32, px33) = pixel_3
                    (px41, px42, px43) = pixel_4

                    # saturates color by RGB values
                    red = (px11 + px21 + px31 + px41) / 4
                    green = (px12 + px22 + px32 + px42) / 4
                    blue = (px13 + px23 + px33 + px43) / 4

                    r = [0, 0, 0, 0]
                    g = [0, 0, 0, 0]
                    b = [0, 0, 0, 0]

                    # gets quadrant color
                    for x in range(0,4):
                        r[x] = custom_filter_saturation(red, x)
                        g[x] = custom_filter_saturation(green, x)
                        b[x] = custom_filter_saturation(blue, x)

                    # puts modified pixel values into the picture
                    pixel_map[i, j] = (r[0], g[0], b[0])

                    if image.size[0] != i + 1:
                        pixel_map[i + 1, j] = (r[1], g[1], b[1])

                    if image.size[1] != j + 1:
                        pixel_map[i, j + 1] = (r[2], g[2], b[2])

                    if image.size[0] != i + 1 and image.size[1] != j + 1:
                        pixel_map[i + 1, j + 1] = (r[3], g[3], b[3])

            picture_with_last_modification_was_saved = False

        # rotates the picture some amount of degrees
        elif command == "Rotate" or command == "rotate":
            rotation_degrees = input("How much degrees you would like to rotate the picture? ")
            if rotation_degrees.isnumeric() == True:
                rotation_degrees = int(rotation_degrees)
                image = image.rotate(rotation_degrees)
                picture_with_last_modification_was_saved = False
                error = False

            else:
                print("Error! Please input a numeric value.")
                error = True

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
                    error = False
                    command = "end the loop"

                elif save_confirmation == "No" or save_confirmation == "no":
                    # splits the file path into file name and the rest of the directory path
                    file_path, file_name = os.path.split(storage_folder + "\\" + picture)
                    # calls save function from image_save.py file
                    image_save.image_save(image, file_name)
                    error = False
                    command = "end the loop"

                else:
                    print("Error! Please choose 'Yes' or 'No'.")
                    error = True

            else:
                command = "end the loop"

        elif command == "Exit" or command == "exit":
            exit = True
            break

        else:
            print("Error! Wrong command. Please input 'Help' to get a list of "
                  "available filters and modifications.")
