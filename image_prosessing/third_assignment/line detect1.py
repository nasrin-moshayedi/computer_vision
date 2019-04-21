# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:51:24 2019

@author: Nasrin Moshayedi
"""

import cv2
import numpy as np


img = cv2.imread('th.jpg') #read image

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #gray picture

blur_gray = cv2.GaussianBlur(gray, (1, 1), 1)

edges = cv2.Canny(blur_gray,10,10,apertureSize = 5) #find edges with canny

#imshape = edges.shape 

lines = cv2.HoughLines(edges,1,np.pi/90,10) #make array of pixels and radians


print(lines) #print array
print(len(lines)) #print array length


#for m in range(1000): #m in m*x+b
for b in range (6): 
    for rho,theta in lines[b]: #for count x and b in m*x +b
        a = np.cos(theta)
        b = np.sin(theta)
            #print(rho)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(179, 100, 255),1)  
        
        
cv2.imshow('detectionmf', img) #display image
cv2.waitKey(0)

cv2.imwrite('detected.jpg',img) #save image in detected.jpg file