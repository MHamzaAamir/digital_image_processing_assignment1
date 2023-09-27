import numpy as np
import cv2 as cv


image = cv.imread("coins.png")

height = image.shape[0]
width = image.shape[1]

new_image = np.zeros((height,width),dtype=np.uint8)

for i in range(height):
    for j in range(width):
        red = image[i][j][0]
        green = image[i][j][1]
        blue = image[i][j][2]

        intensity =  0.333 * red +  0.333 * green + 0.333 * blue


        if(intensity < 140):
            intensity = 0
        else:
            intensity = 255
        
        new_image[i][j] = intensity
    
cv.imshow("pic",new_image)
cv.waitKey(0)
        

