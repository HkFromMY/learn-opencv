import cv2
import numpy as np
import random

img = cv2.imread('images\\colorcolor.jpg')
print(img.shape) # (1015, 700, 3)

# in opencv python the color channels are arranged in B G R instead of R G B

rand_img = np.empty((300, 300, 3), np.uint8)
for row in range(300):
    for col in range(300):
        rand_img[row][col] = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ] # B G R

new_img = img[:150, :200] # [y, x]
cv2.imshow('New img', new_img)
cv2.imshow('Ori', img)
cv2.imshow('Random Img', rand_img)
cv2.waitKey(0)