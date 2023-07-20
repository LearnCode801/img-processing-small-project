import numpy as np
import cv2

# Reading the image and resize  it
img = cv2.imread('C:/Users/Muhammad Talha Awan/Desktop/2.png')
img = cv2.resize(img, (1000, 500))

# Converting it into the Grayscle
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creating the trackbars


def cross(x):
    pass


cv2.namedWindow('color_Adjestments', cv2.WINDOW_NORMAL)
cv2.resizeWindow('color_Adjestments', (300, 300))

cv2.createTrackbar('scale', 'color_Adjestments', 0, 255, cross)
cv2.createTrackbar('color', 'color_Adjestments', 0, 255, cross)


# Step 2
while True:
    scale = cv2.getTrackbarPos('scale', 'color_Adjestments')
    color = cv2.getTrackbarPos('color', 'color_Adjestments')

    # Extracting color code
    # step ---> 3
    inverted_gray = color - gray  # inverted color image
    cv2.imshow("inverted_gray", inverted_gray)

    # step ---> 4
    blur_img = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    cv2.imshow("blur_img", blur_img)

    # step ---> 5
    inverted_blur = color - blur_img  # inverted blured image
    cv2.imshow("inverted_blur", inverted_blur)

    pencil_scatch = cv2.divide(gray, inverted_blur, scale=scale)

    cv2.imshow("pencil_scatch", pencil_scatch)
    cv2.waitKey(1)


cv2.destroyAllWindows()
