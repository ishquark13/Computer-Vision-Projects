'''
import glob
from PIL import Image

list_of_files = glob.glob('/testing_data/redCars./*.png')           # create the list of the images
for file_name in list_of_files:
    im1 = Image.open(file_name)
    im2 = im1.rotate(90)
    for line in im2:
       im2.save(line + "90")
'''

#import require libraries
from PIL import Image
import glob
import os


# Find all the jpegs/pngs in a given folder:
folder='.\testing_data\whiteCars'
imList=glob.glob(folder+'*.png')


# Loop through all the image:
for img in imList:
    # open the image
    im1 = Image.open(img)
    # extract the filename and extension from path
    fileName, fileExt = os.path.splitext(img)
    #rotate image
    im2 = im1.rotate(90)
    # save the image in the same folder, with the same name, except *.png
    im2.save(folder+fileName+'90'+'.png')        