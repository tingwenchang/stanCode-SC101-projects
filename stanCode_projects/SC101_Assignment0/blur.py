"""
File: blur.py
Name: Ting-Wen (Wenny)
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred image from the original one
    """
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            new_img_pixel = new_img.get_pixel(x, y)

            total_red = 0
            total_blue = 0
            total_green = 0
            count = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and i < img.width and j >= 0 and j < img.height:
                        total_red += img.get_pixel(i, j).red
                        total_blue += img.get_pixel(i, j).blue
                        total_green += img.get_pixel(i, j).green
                        count += 1

            new_img_pixel.red = total_red / count
            new_img_pixel.blue = total_blue / count
            new_img_pixel.green = total_green / count
    return new_img


def main():
    """
    This program is to change the original image to a blurred one, by creating the same range image blank and
    averaging the neighborhood pixels.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
