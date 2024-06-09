import cv2
import numpy as np

# kernel size
kernel1 = np.ones((3, 3), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)

img = cv2.imread('images\\colorcolor.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# convert color
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert color scale from B G R  to gray

# blur image
# parameters: [img_var, tuple of kernel size, sigma/standard deviation]
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0) # kernel size (k-size) must be possing 2 same odd number

# get edges of an image
# parameters: [img_var, min_threshold, max_threshold]
find_edge = cv2.Canny(img, 150, 200)

# expand image (make edges bolder)
# parameters: [canny object, kernel with np.ones, iterations #]
dilated = cv2.dilate(find_edge, kernel1, iterations=1)

# opposite of dilate
# parameters: [maybe dilate object, kernel, iterations]
eroded = cv2.erode(dilated, kernel2, iterations=1)

# cv2.imshow('Image', img)
# cv2.imshow('Gray', gray_img)
# cv2.imshow('Blur', gaussian_blur)
cv2.imshow('Find Edge', find_edge)
cv2.imshow('dilated', dilated)
cv2.imshow('eroded', eroded)
cv2.waitKey(0)