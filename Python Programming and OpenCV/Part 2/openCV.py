import numpy as np
import cv2

from PIL import Image


def detect_red_and_white_regions(image):
    img = cv2.imread(image, -1)
    smallImg = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
    cv2.imshow("Original-Small", smallImg)

    hsvImg = cv2.cvtColor(smallImg, cv2.COLOR_BGR2HSV)

    red_lower = np.array([136, 87, 111], dtype=np.uint8)
    red_upper = np.array([178, 255, 255], dtype=np.uint8)
    red_mask = cv2.inRange(hsvImg, red_lower, red_upper)
    res_red = cv2.bitwise_and(smallImg, smallImg, mask=red_mask)
    cv2.imshow("Red", res_red)

    white_lower = np.array([0, 0, 200], dtype=np.uint8)
    white_upper = np.array([180, 30, 255], dtype=np.uint8)
    white_mask = cv2.inRange(hsvImg, white_lower, white_upper)
    res_white = cv2.bitwise_and(smallImg, smallImg, mask=white_mask)
    cv2.imshow("White", res_white)

    white_red = cv2.addWeighted(res_red, 1.0, res_white, 1.0, 0.0)
    cv2.imshow("White_Red", white_red)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def analyze_goat(image_array):
    # Print Minimum and maximum pixel values in the image
    max_value = np.max(image_array)
    min_value = np.min(image_array)
    print("Maximum pixel value: ", max_value)
    print("Minimum pixel value: ", min_value)

    # Print Average pixel value in the image
    average_pixel = int(np.mean(image_array))
    print("Average_pixel: ", average_pixel)

    # Print Total number of non-zero pixels in the image
    shape = image_array.shape
    print("Shape of the image: ", shape)

    non_zero_pixels = np.count_nonzero(image_array)
    print("Total number of non-zero pixels: ", non_zero_pixels)

    # Print Total number of zero pixels in the image
    zero_pixels = np.prod(shape) - non_zero_pixels
    print("Total number of zero pixels: ", zero_pixels)


if __name__ == '__main__':

    goat = "img/Goat.jpg"
    detect_red_and_white_regions(goat)

    img = Image.open("img/Goat.jpg")
    img_data = np.asarray(img)
    analyze_goat(img_data)
