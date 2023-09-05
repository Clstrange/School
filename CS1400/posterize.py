"""
File: posterize.py
Project 7.5

Defines and tests a function for posterizing images.
"""

from images import Image


""" Write your code here """

def main():
    filename = input("Enter the image file name: ")
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input("Enter an integer [0..255] for green: "))
    blue = int(input("Enter an integer [0..255] for blue: "))                    
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()

if __name__ == "__main__":
   main()

