# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 14:41:21 2018

@author: vkumar
"""

import cv2

img = cv2.imread('Fruits.jpg',1)
print(img)

cv2.imshow('Banana',img)
cv2.waitkey(0)
print(img[100,100])
cv2.destroyAllWindows()