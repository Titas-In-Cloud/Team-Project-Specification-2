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
image manipulation library installed (it is a fork of the Python Imaging Library 
(PIL)). To install the Pillow module please write the code specified below in 
```Terminal```:
```
 pipenv install pillow 
```
## Usage
Before using the package make sure that the directory path in ```Terminal``` 
ends with '\specification-2'. \
There are specific functions which need to be performed for different types of 
functionalities. Run code below in ```Terminal``` if you want to:
 1. Pick the pictures that need to be modified - ```pipenv run python main.py storage```
    * Write the full directory path starting from the parent directory (which 
    should be: ..\practical-3\specification-2) when choosing the picture folder.
    * Write the full directory path starting from the parent directory (which 
    should be: ..\practical-3\specification-2) and full file name with extension 
    when choosing the file.
    * Follow further instructions in ```Terminal``` for storing the pictures 
    for modification.
 2. See the list of picked pictures - ```pipenv run python main.py list```
 3. Create JPEG thumbnails of chosen pictures - ```pipenv run python main.py thumbnail```
    * Follow instructions in ```Terminal``` to set the size of JPEG thumbnails 
    and directory where the thumbnails will be saved.
    * If the inputted directory does not exist the package will automatically create one.
 4. Start the modification process of the chosen pictures - ```pipenv run python 
 main.py filters```
    * After you started the modification process, please input help for a list of 
    available filters.
    * Follow the instructions and messages in the ```Terminal``` for each step 
    during the modification process.
    * During the save process if the inputted directory does not exist the package
    will automatically create one.
 5. Get a list with function names and their functionality - ```pipenv run python 
 main.py --help```
 
## License
This project is licensed under the MIT License - see the **LICENSE.md** file for
details.
