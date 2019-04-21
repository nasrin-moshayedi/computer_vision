# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:55:53 2019

@author: nasrin moshayedi
"""

import cv2
import numpy as np


filename = "download.jpg"
k = 1
t = 200

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
#cv2.waitKey(0)

blur = cv2.GaussianBlur(img, (k, k), 0)
(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)


edgeX = cv2.Sobel(binary, cv2.CV_64F, 1, 0)
edgeY = cv2.Sobel(binary, cv2.CV_64F, 0 , 1)


edgeX = np.uint8(np.absolute(edgeX))
edgeY = np.uint8(np.absolute(edgeY))
edge = cv2.bitwise_or(edgeX, edgeY)

# display edges
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.imshow("edges", edge)
cv2.waitKey(0)
