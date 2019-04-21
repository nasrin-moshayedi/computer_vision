# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:41:39 2019

@author: nasrin moshayedi
"""

import cv2

img = cv2.imread("temp.jpg") #read orginal image
gray = cv2.imread("temp.jpg" , cv2.IMREAD_GRAYSCALE) #read grayscale image and save in variable

cv2.imshow("Grayscale", gray) # frist argument is windows lable
cv2.waitKey(0)
