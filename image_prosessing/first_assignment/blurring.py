# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:37:46 2019

@author: nasrin moshayedi
"""

import cv2
k = 45 #burred zoom
filename = "temp.jpg" #image file name

img = cv2.imread(filename) #read image
cv2.namedWindow("orignal", cv2.WINDOW_NORMAL) #create a window normal size
cv2.imshow("orignal", img) #show image
#cv2.waitKey(0) # if we didn't write this line image will not show

#display blurred image
blurred = cv2.blur(img, (k,k))
cv2.namedWindow("blurred" , cv2.WINDOW_NORMAL) #create normal window for blure image
cv2.imshow("blurred", blurred) #show blurred image
cv2.waitKey(0) 