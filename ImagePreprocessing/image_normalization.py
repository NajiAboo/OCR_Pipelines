"""
 3 methods to normalize the image
"""

import cv2
import numpy as np

def devide_by_max(img):
    """
    Devide the image by max value ie 255
    """
    return img/255

def min_max(img):
    """'
     x = (x - xmin ) / (xmax-xmin)
    """
    x_min = np.min(img)
    x_max = np.max(img)
    return ( (img - x_min) / (x_max-x_min))

def standardize(img):
    """
     x = x - x_mean / x_zigma
    """
    x_mean = np.mean(img)
    x_std  = np.std(img)
    return ((img-x_mean)/x_std)