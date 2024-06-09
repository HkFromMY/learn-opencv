import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread("images\\XiWinnie.jpg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)


# create window for trackbars
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 320)
cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

# before detecting color, we need to convert the color scale to HSV value
hsv_recolored = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    # get value at trackbar
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')

    print(
        "Hue Min:", str(h_min) + "\n",
        "Hue Max:", str(h_max) + "\n",
        "Sat Min:", str(s_min) + "\n",
        "Sat Max:", str(s_max) + "\n",
        "Val Min:", str(v_min) + "\n",
        "Val Max:", str(v_max) + "\n",
    )
    # all minimum hsv value
    lower = np.array([
        h_min,
        s_min,
        v_min
    ])
    # all maximum hsv value
    upper = np.array([
        h_max,
        s_max,
        v_max
    ])

    # apply the hsv recolored img and all hsv value to be convered to a mask
    mask = cv2.inRange(hsv_recolored, lower, upper) # mask that will be used for filtering color
    # the white color part at mask img will be remained at the img if using the code below
    filtered_img = cv2.bitwise_and(img, img, mask=mask) # filter and detect color

    # show all the images
    cv2.imshow('original img', img)
    cv2.imshow('hsv recolored', hsv_recolored)
    cv2.imshow('mask', mask)
    cv2.imshow('result', filtered_img)
    cv2.waitKey(1)


