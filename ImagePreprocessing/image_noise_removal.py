#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 07:04:09 2021

@author: sfm
"""
 
"""
 Noise Removal
 
 There are different type of noice 
 1. salt and pepper noise
 2. gaussian noise
 3. speckle noise
 4. poisson noise
 
 Based on the noise we will use different techniques
 
 eg: salt and pepper we use Median filtering 
 Gaussian Noise -> Gaussian filetering 
"""

import cv2

noise_img = cv2.imread("saltpepper.jpg")
#cv2.imshow("salt and pepper", noise_img)
#cv2.waitKey(0)

out = cv2.medianBlur(noise_img, 5)
cv2.imshow("noise_removed", out)
cv2.imshow("salt and pepper", noise_img)
cv2.waitKey(0)







