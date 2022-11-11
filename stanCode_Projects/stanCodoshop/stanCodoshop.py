"""
File: stanCodoshop.py
Name: David Lin
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    dist = ((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    rgb = []
    red = 0
    green = 0
    blue = 0
    n = len(pixels)
    for i in range(n):
        # adding RGB value
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    rgb.append(int(red/n))
    rgb.append(int(green/n))
    rgb.append(int(blue/n))
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    dist_lst = []
    red = 0
    green = 0
    blue = 0
    n = len(pixels)
    for i in range(n):
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    red_avg = int(red / n)
    green_avg = int(green / n)
    blue_avg = int(blue / n)
    for i in range(n):
        dist = ((red_avg - pixels[i].red) ** 2 + (green_avg - pixels[i].green) ** 2 + (blue_avg - pixels[i].blue) ** 2) ** 0.5
        dist_lst.append(dist)
    best_pixel_index = dist_lst.index(min(dist_lst))    # get minimum distance pixel's index in the list
    return pixels[best_pixel_index]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    pix_list = []
    n = len(images)
    for y in range(height):
        for x in range(width):
            for i in range(n):
                pix = images[i].get_pixel(x, y)
                pix_list.append(pix)    # make a list which contain all images' pixels at same coordinates
            result.set_pixel(x, y, get_best_pixel(pix_list))    # assign the best pixel in blank image
            pix_list = []       # refresh pixel list


    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()