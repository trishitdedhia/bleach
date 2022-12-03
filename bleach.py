#!/bin/python
from PIL import Image
import sys

#Get image
img = Image.open(sys.argv[1])

#Convert image to rgb
img = img.convert('RGBA')

#Get image data
data = img.getdata()
newdata = []

#Get Colour
print("Enter the the RGB value of bleach colour.")
code = []
code.append(int(input("R : ")))
code.append(int(input("G : ")))
code.append(int(input("B : ")))

#Get image size and initialise progress
size = img.size
progress = 0

#Run a loop for each pixel
print("Processing Image...", end="")
for px in data:

    #Check if the pixel matches
    newdata.append((code[0], code[1], code[2], px[3]))


    
#End process Image
print("\rImage Processed.")

#Put data and save image
img.putdata(newdata)
img.save(sys.argv[2])






