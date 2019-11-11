import os
from PIL import Image
from PIL import ImageFilter

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

print("Please input 'Help' to get a list of available filters and modifications. ")

command = "start the loop"

for picture in os.listdir(storage_folder):
    image = Image.open(storage_folder + "\\" + picture)
    picture_with_last_modification_was_saved = True
    # creates picture pixel map
    pixel_map = image.load()
    print(picture + " was picked for modification.")
    while command != "End":
        command = input("What would you like to do? ")

        # prints a list with available commands
        if command == "Help" or command == "help":
            print("List of filters and modifications:")
            print(" * Show - shows the picture with applied filters \n"
                  " * Blur - applies blur filter to the picture \n"
                  " * Contour - applies contour filter to the picture \n"
                  " * Emboss - applies emboss filter to the picture \n"
                  " * Enhance - applies enhance filter to the picture \n"
                  " * Greyscale - applies custom greyscale filter \n"
                  " * Dither - applies custom dithering filter \n"
                  " * Rotate - rotates the picture in inputed amount degrees \n"
                  " * Cancel - cancels all filters applied to the picture \n"
                  " * Save - saves the picture \n"
                  " * End - ends modification process")

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

        # applies custom greyscale filter to the picture
        elif command == "Greyscale" or command == "greyscale":
            for i in range(image.size[0]):
                for j in range(image.size[1]):
                    red, green, blue = pixel_map[i, j]
                    pixel_brightness = int(round(0.299 * red + 0.587 * green + 0.114 * blue))
                    pixel_map[i, j] = (pixel_brightness, pixel_brightness, pixel_brightness)

            picture_with_last_modification_was_saved = False

        # applies custom dithering filter to the picture
        elif command == "Dither" or command == "dither":
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

                    # puts dithered pixel values into the picture
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