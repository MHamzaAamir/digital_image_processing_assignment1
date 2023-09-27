import cv2 as cv
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

        intensity =  0.14 * red +  0.57 * green + 0.29 * blue


        if(intensity < 140):
            intensity = 255
        else:
            intensity = 0
        
        new_image[i][j] = intensity

num_labels, labeled_image = cv.connectedComponents(new_image)

print("Coins:",num_labels-1)

cv.imshow("binary",new_image)
cv.waitKey(0)