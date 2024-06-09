import cv2
img = cv2.imread('images\\lenna.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

model = cv2.CascadeClassifier('face_detect.xml')
# after detecting the image for 1 round, then the model will resize the image to smaller scale according to the scale factor passed into the method
# if 3 (passed in min neighbors) rectangle is in the same area then it means the face is there 
faceRect = model.detectMultiScale(gray, 1.1, 3)

# bound the face with a rectangle
for (x, y, width, height) in faceRect: 
    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)

cv2.imshow('Img', img)
cv2.waitKey(0)