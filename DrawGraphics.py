import cv2
import numpy as np

# draw shape with opencv
blank_img = np.zeros(shape=(600, 600, 3), dtype=np.uint8)
cv2.line(blank_img, pt1=(0, 0), pt2=(400, 300), color=(255, 255, 255), thickness=3)
cv2.line(blank_img, (0, 0), (blank_img.shape[1], blank_img.shape[0]), (0, 255, 0), 2)
cv2.rectangle(blank_img, (0, 0), (200, 200), (255, 0, 0), cv2.FILLED) # filled the shape
cv2.circle(blank_img, (300, 400), 30, (0, 0, 255), 3)
cv2.putText(blank_img, "HELLO WORLD", (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 12, 31), 3)

cv2.imshow('Img', blank_img)
cv2.waitKey(0)