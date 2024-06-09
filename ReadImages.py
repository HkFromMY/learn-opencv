import cv2

# read an image
# img = cv2.imread('images\\colorcolor.jpg')
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# cv2.imshow('se se img', img)
# cv2.waitKey(0)

# read a video with mp4 files
# video_cap = cv2.VideoCapture('images\\thumb.mp4')

# while True:
#     ret, frame = video_cap.read() # returns ret (boolean) and frame (image to show)
#     if ret:
#         frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#         cv2.imshow('thumb video', frame)
#     else:
#         break
#     # cv2.waitKey(1) # can adjust the speed of video playing
#     if cv2.waitKey(10) == ord('q'):
#         break;

# read a video with webcam
# 0 means default webcam while 1 means external webcam
video_webcap = cv2.VideoCapture(0)

while True:
    ret, frame = video_webcap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=2, fy=2)
        cv2.imshow('My Webcam', frame)

    else:
        break

    if cv2.waitKey(10) == ord('q'):
        break;
