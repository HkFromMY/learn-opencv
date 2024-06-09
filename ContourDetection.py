import cv2

img = cv2.imread('images\\shape.jpg')
img_contour = img.copy()

# convert the image to gray scale first then convert into canny object to be used for contour finding
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    contour_area = cv2.contourArea(contour)
    if contour_area > 500:
        # if the contour index is -1 then draw every contours point found
        cv2.drawContours(img_contour, contour, -1, (255, 0, 0), 3)

        # get area of contour
        print("Area of contour:", cv2.contourArea(contour))

        # get arc length of the contour (second parameter in arcLength method if whether the shape is closed)
        perimeter = cv2.arcLength(contour, True)
        print("Arc Length of contour", perimeter)

        # get the number of vertices of the contour
        vertices = cv2.approxPolyDP(contour, perimeter * 0.02, True)
        print("# of vertices of the contour", vertices.shape[0])
        
        # use rectangle to enclose the shape detected by passing in vertices point
        # returns 4 values which is left bottom x and y, width and height
        x, y, width, height = cv2.boundingRect(vertices)
        cv2.rectangle(img_contour, (x, y), (x + width, y + height), (0, 255, 0), 3)
        
        if vertices.shape[0] == 3:
            cv2.putText(img_contour, "Triangle", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

        elif vertices.shape[0] == 4:
            cv2.putText(img_contour, "Rectangle", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

        elif vertices.shape[0] == 5:
            cv2.putText(img_contour, "Pentagon", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

        else:
            cv2.putText(img_contour, "Circle", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

        print("\n")


cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.imshow('contour', img_contour)
cv2.waitKey(0)