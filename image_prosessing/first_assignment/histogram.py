# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:54:48 2019

@author: nasrin moshayedi
"""

import cv2

from matplotlib import pyplot as plt #install it in virtuall machine

img = cv2.imread("temp.jpg" , cv2.IMREAD_GRAYSCALE) #read image as gray image
imag = cv2.imread("temp.jpg") #read image as gray image

cv2.namedWindow("GrayScale Image", cv2.WINDOW_NORMAL) #creat a normal window
cv2.imshow("GrayScale Image", img)
#cv2.imshow("GRAY" , img) #show gray image with a GRAY lable
cv2.waitKey(0) #show image without delay

histogram = cv2.calcHist([img], [0], None, [255], [0, 55])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 256])

plt.plot(histogram)
plt.show()
