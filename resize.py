import numpy as np
import cv2 as cv

image = cv.imread("coins.png")

height = 256
width = 256

image = cv.resize(image,(width,height))

cv.imshow("pic",image)
cv.waitKey(0)
