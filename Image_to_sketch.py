#Importing libraries

import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw, ImageOps

#Input the image
image = cv2.imread('F:/ACM/ASCII/dark.jpg')

#Converting the image to B/W
BW_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#-------------------------------------------------------------------------------------------------------------------#
#Defining the Character Map
Character = {
    "standard" : "@%#*+=:. ",
    "complex" : "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

#Defining the function to make font object, scale, and char_list
def char_data(mode):
    font = ImageFont.truetype("F:/ACM/ASCII/DejaVuSansmono.ttf", 10)
    scale = 2 #To equalize the height and width
    char_list = Character[mode]
    return char_list, font, scale

#Setting the background black or white
background = "white"
if background == "white":
    bg_code = 255
elif background == "black":
    bg_code = 0

#Initialising the char_list, font, scale
char_list, font, scale = char_data("complex")
num_chars = len(char_list)
num_col = 585 #depends upon the selected image


#-------------------------------------------------------------------------------------------------------------------#
#CONVERTING THE IMAGE TO PENCIL SKETCH

inverted_image = 255 - BW_image
blur_image = cv2.GaussianBlur(inverted_image, (21,21), 0)
inverted_image_blur = 255 - blur_image

#Converting the B/W image to pencil sketch
sketch_image = cv2.divide(BW_image, inverted_image_blur, scale=256.0)

#Saving the Pencil sketched image
cv2.imwrite("F:/ACM/ASCII/dark_sketch.jpg", sketch_image)


#-------------------------------------------------------------------------------------------------------------------#
#CONVERTING THE SKETCH IMAGE TO ASCII IMAGE
#Here we already converted our image to shaded pencil form,
#Now if we use the character mapping we'll get the final result

image = sketch_image

#Height and Width of the image
height, width = sketch_image.shape

#Height and Width of each pixel in image
pixel_width = width/num_col
pixel_height = scale * pixel_width
num_row = int(height/pixel_height)

#Height and Width of ASCII image
char_w, char_h = font.getsize("A")
final_width = char_w*num_col
final_height = scale*char_h*num_row

#Making new image
ascii_image = Image.new("L",(final_width, final_height), bg_code)
ascii_draw = ImageDraw.Draw(ascii_image)

#Placing the characters
for i in range(num_row):
    min_h = min(int((i+1)*pixel_height), height)
    row_pix = int(i*pixel_height)
    line = "".join([char_list[min(int(np.mean(image[row_pix:min_h, int(j*pixel_width):min(int((j+1)*pixel_width), width)]) / 255 * num_chars), num_chars - 1)]for j in range(num_col)]) + "\n"

    #Making and storing the string by character mapping
    ascii_draw.text((0, i*char_h), line, fill=255-bg_code, font=font)

#Inverting the image and removing excess border
if background == "black":
    crop_image = ascii_image.getbbox()
elif background == "white":
    crop_image = ImageOps.invert(ascii_image).getbbox()

#Saving the ASCII Image
ascii_image = ascii_image.crop(crop_image)
ascii_image.save("F:/ACM/ASCII/dark_pencil_sketch.jpg")