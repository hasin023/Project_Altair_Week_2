import numpy as np
import cv2

img = cv2.imread('img/GOAT.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)


hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvImg, red_lower, red_upper)
res_red = cv2.bitwise_and(img, img, mask=red_mask)
cv2.imshow("Red", res_red)


white_lower = np.array([0, 0, 200], np.uint8)
white_upper = np.array([180, 30, 255], np.uint8)
white_mask = cv2.inRange(hsvImg, white_lower, white_upper)
res_white = cv2.bitwise_and(img, img, mask=white_mask)
cv2.imshow("White", res_white)

cv2.waitKey(0)
cv2.destroyAllWindows()
