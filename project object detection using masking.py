import numpy as np
import cv2


def nothing(x):
    pass


img = cv2.imread(
    'E:/Full Stack Data Scientist Bootcamp/Deep Learning/Open CV/image processing/color ball img.jpg')
img = cv2.resize(img, (400, 300))

cv2.namedWindow('color_adjestments')

cv2.createTrackbar('lower_h', 'color_adjestments', 0, 255, nothing)
cv2.createTrackbar('lower_s', 'color_adjestments', 0, 255, nothing)
cv2.createTrackbar('lower_v', 'color_adjestments', 0, 255, nothing)

cv2.createTrackbar('upper_h', 'color_adjestments', 255, 255, nothing)
cv2.createTrackbar('upper_s', 'color_adjestments', 255, 255, nothing)
cv2.createTrackbar('upper_v', 'color_adjestments', 255, 255, nothing)

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('lower_h', 'color_adjestments')
    l_s = cv2.getTrackbarPos('lower_s', 'color_adjestments')
    l_v = cv2.getTrackbarPos('lower_v', 'color_adjestments')

    u_h = cv2.getTrackbarPos('upper_h', 'color_adjestments')
    u_s = cv2.getTrackbarPos('upper_s', 'color_adjestments')
    u_v = cv2.getTrackbarPos('upper_v', 'color_adjestments')

    upper_bound = np.array([u_h, u_s, u_v])
    lower_bound = np.array([l_h, l_s, l_v])

    print(upper_bound)
    print(lower_bound)
    print("talha")

    # creating the mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Appling the Mask or the filterign the image
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    cv2.waitKey(1)
