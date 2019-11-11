# CSC1034: Practical 3 - Specification 2
This package allows user to modify and apply filters to the pictures.
## Description
Package was created during the third practical of the **CSC1034** course 
while working on a group project and  is intended to be used for modifying, 
applying filters and saving modified different types of images in a user-friendly 
manner. There are numbers of filters which user can apply to the chosen pictures, 
this includes blur, emboss, greyscale, enhance and a lot more.

## Installation
This package runs on Python version 3.7 or above and needs additional Pillow 
image manipulation module installed. To install the Pillow package please
write the code specified below in ```Terminal```:
```
 pipenv install pillow 
```
## Usage
There are specific functions which needs to be run for different types of 
functionalities. Run code below in ```Terminal``` if you want to:
 1. Pick the pictures that needs to be modified - ```pipenv run python main.py storage```
 2. See the list of picked pictures - ```pipenv run python main.py list```
 3. Create JPEG thumbnails of chosen pictures - ```pipenv run python main.py thumbnail```
 4. Start the modification process of the chosen pictures - ```pipenv run python main.py filters```
## License
This project is licensed under the MIT License - see the **LICENSE.md** file for
details.
