import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread("coins.png")

height = image.shape[0]
width = image.shape[1]

new_image = np.zeros((height,width),dtype=np.uint8)

for i in range(height):
    for j in range(width):
        red = image[i][j][0] 
        green = image[i][j][1]
        blue = image[i][j][2]

        a = 0.299 * red + 0.587 * green + 0.114 * blue

        new_image[i][j] = int(a)
        

cv.imshow("pic",new_image)

cv.waitKey(0)