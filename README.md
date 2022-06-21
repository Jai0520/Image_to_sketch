# Image To Sketch

## Project Description
ASCII or American Standard Code for Information Interchange is a common encoding format used for representing strings and text data in computers.
In this project we will be seeing how we can form an ASCII art version of an image.

## How to run the project
* you can use git clone command to download the contents of the project.

$ git clone https://github.com/Jai0520/Image_to_sketch

* Once you have the folder and the files in your system open the Image_to_sketch.py file in your editor and run the python file.

> python Image_to_sketch.py

> Note : above command maybe different according to the version of python installed in your system so check it accordingly like using python3 command instead of python.

## Description of my tasks
* Taking an image as an input and forming a pencil sketched version of the image but only with ascii characters embedded in it.

## The internal working of the project
* Each individual color is represented by numbers ranges between 0 to 255. Images are composed of pixels each having its value between 0 to 255, which can be denoted by ASCII characters.
* In this project firstly the image is converted to grayscale (B/W) then into an inverted image using an open source linbrary OpenCV
* Now using the character mapping to convert the grey area into ASCII charcters based on the luminosity of each pixel which generates the pencil sketch version of input image consisting of ASCII characters

## My learnings from the project
* Through this project I got to learn about how images are being processed in computer using OpenCV library
* Learned about how each ASCII character can be distinguish based on the luminosity, for example, "," can be used to cover the light region of the image and "$" can be used in darker region if the image.

## Resources
* [Drawing an Ascii sketch](https://blog.waffles.space/2017/03/01/ascii-sketch/#fnref:2)
* [AScii Art](https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles)
