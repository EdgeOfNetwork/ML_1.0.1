import numpy as np
import cv2

'''
Problem #1 Image Transformations
'''

# 1-1
def translate(image, x, y):
    # Write your code
    translation_matrix = np.array(...)

    transformed_image = cv2.warpAffine(...)

    return transformed_image

def rotate(image, angle):
    # Write your code
    translation_matrix = np.array(...)

    transformed_image = cv2.warpAffine(...)

    return transformed_image

def similarity(image, x, y, angle, scale):
    # Write your code
    translation_matrix = ...

    transformed_image = cv2.warpAffine(...)

    return transformed_image

'''
Problem #2 Linear Filters
'''

# 2-1

def average_image(image):
    # Write your code
    # You can make any-size average filter
    filter = np.array(...)

    result = cv2.filter2D(...)

    return result

def sharpen_image(image):
    # Write your code
    # You can make any kind of sharpening filter
    filter = np.array(...)

    result = cv2.filter2D(...)

    return result

# 2-2

def Gaussian_blur(image):
    # Write your code
    # Set any size and sigma
    filter = cv2.GaussianBlur(...)

    result = cv2.filter2D(...)

    return result

# 2-3

def add_salt_pepper_noise(image, prob):
    # Write your code
    # You can use prob argument as the probability of noise at each pixel
    noise = ...

    result = ...

    return result

# Write your code
# Apply average, sharpening, and GaussianBlur to the result image with noise
...

# 2-4

def median_blur(image):
    # Write your code
    # You can use cv2.medianBlur
    # Choose various sizes of the filter
    filter = cv2.medianBlur(...)

    result = ...

    return result

# Write your code
# Apply medianBlur to the result image with noise
...

'''
Problem #3 Image Pyramids
'''

# 3-1

# Use cv2.resize() and its argument "interpolation=..."
# Try different options of interpolation

# Write your code
# To down-sample an image, you should set the size smaller than the image
down_result_01 = cv2.resize(..., interpolation=...)
down_result_02 = cv2.resize(..., interpolation=...)
down_result_03 = cv2.resize(..., interpolation=...)

# Write your code
# To up-sample an image, you should set the size lager than the image
up_result_01 = cv2.resize(..., interpolation=...)
up_result_02 = cv2.resize(..., interpolation=...)
up_result_03 = cv2.resize(..., interpolation=...)

# 3-2

# Write your code
# Set the number of levels of pyramid as many as you want
Gaussian_01 = cv2.pyrDown(...)
Gaussian_02 = cv2.pyrDown(...) # You should use Gaussian_01 as the input
... # You can repeat

'''
Problem #4 Median Blur
'''
def my_median_blur(image, size):
    # Write your code
    # You can use any library for sorting like numpy.sort()
    # You do not have to consider the issue of padding

    ...

    return result