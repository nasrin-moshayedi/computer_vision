# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:50:01 2019

@author: nasrin moshayedi
"""

import cv2

def cannyEdge():
	global img, minT, maxT
	edge = cv2.Canny(img, minT, maxT)
	cv2.imshow("edges", edge)


def adjustMinT(v):
	global minT
	minT = v
	cannyEdge()


def adjustMaxT(v):
	global maxT
	maxT = v
	cannyEdge()
	

filename = "download.jpg"

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
minT = 150
maxT = 150

cv2.createTrackbar("minT", "edges", minT, 255, adjustMinT)
cv2.createTrackbar("maxT", "edges", maxT, 255, adjustMaxT)

cannyEdge()
cv2.waitKey(0)