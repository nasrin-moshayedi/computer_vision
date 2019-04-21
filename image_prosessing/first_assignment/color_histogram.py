# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 07:52:14 2019

@author: Asus
"""

import cv2
import sys
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
img = cv2.imread("temp.jpg")

# display the image 
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# split into channels
channels = cv2.split(img)

# list to select colors of each channel line
colors = ("b", "pink", "r") 

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for(channel, c) in zip(channels, colors):
    histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(histogram, color = c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()