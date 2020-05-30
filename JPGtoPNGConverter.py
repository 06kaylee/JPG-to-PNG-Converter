import sys
import os
from PIL import Image


#get first and second arguments
try:
    src_folder = sys.argv[1]
    dest_folder = sys.argv[2]
except IndexError as err:
    #if none are provided ask the user directly
    if len(sys.argv) == 1:
        src_folder = input('Please provide the source directory path: ')
        dest_folder = input('Please provide destination directory path: ')
    #if only the source is provided
    elif len(sys.argv) == 2:
        print(src_folder)
        dest_folder = input('Please provide destination directory path: ')



#check if new path folder exists, if not create
isExist = os.path.isdir(dest_folder)
if(not isExist):
    os.mkdir(dest_folder)
else:
    print("That destination path already exists.")

#loop through file names in Pokedex
for filename in os.listdir(src_folder):
    #open original img
    img = Image.open(f'{src_folder}\\{filename}')
    #get the file name without file extension
    name = os.path.splitext(filename)[0]
    #saves img to new directory with png as extension
    img.save(f'{dest_folder}\\{name}.png', 'png')

