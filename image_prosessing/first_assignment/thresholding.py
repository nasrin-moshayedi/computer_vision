# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:27:56 2019

@author: nasrin moshayedi
"""

import cv2

filename = "download.jpg"
k = 5
t = 156 #find it by test

#read and display original image
img = cv2.imread(filename)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
#cv2.waitKey(0)

#blur and grayscale image
blur = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(blur, (k, k), 0)

#perform inverse binary thresholding
(t, maskLayer) = cv2.threshold(blur, t , 5, cv2.THRESH_BINARY_INV)

#make a mask 
mask = cv2.merge([maskLayer, maskLayer, maskLayer])

cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.imshow("mask", mask)
#cv2.waitKey(0)

sel = cv2.bitwise_and(img, mask)

cv2.namedWindow("shelected", cv2.WINDOW_NORMAL)
cv2.imshow("shelected", sel)
cv2.waitKey(0)
