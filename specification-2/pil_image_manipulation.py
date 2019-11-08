import os
from os import path
from PIL import Image

print(os.getcwd())

command = input("* What do you want to do? ")

while command != "exit":

    file = open("./location.txt", "r")
    Picture = file.read()
    file.close()

    if command == "list":
        for f in os.listdir('..\pictures'):
            if f.endswith('.jpg'):
                print(f)

    elif command == "location":
        # Rewrites the location.txt file (makes it empty and ready to store another location)
        open("./location.txt", "w").close()

        file = open("./location.txt", "r+")
        location = "..\pictures\\"
        location = location + input("What picture would you like to use? Please, write the name of it: ")

        if path.exists(location):
            file.write(location)
            print("Success! Picture was scanned successfully.")
        else:
            print("Error! Picture does not exist.")

        file.close()

    elif command == "show":
        image = Image.open(Picture)
        image.show()

    elif command == "save as jpg":
        image = Image.open(Picture)
        name = input("Please write the name for a new file: ")
        image.save('{}.jpg'.format(name))

    elif command == "save as jpeg":
        image = Image.open(Picture)
        name = input("Please write the name for a new file: ")
        image.save('{}.jpeg'.format(name))

    elif command == "save as png":
        image = Image.open(Picture)
        name = input("Please write the name for a new file: ")
        image.save('{}.png'.format(name))

    elif command == "help":
        print("Command list:")
        print(" * list          - shows the list of the available pictures")
        print(" * location      - sets the location of the image")
        print(" * show          - shows the current image")
        print(" * save as jpg   - saves image as jpg file")
        print(" * save as jpeg  - saves image as jpeg file")
        print(" * save as png   - saves image as png file")
        print(" * exit          - exits the program")

    else:
        print("Error! Invalid command.")

    command = input("* What do you want to do? ")


if command == "exit":
    print("Exited successfully")
