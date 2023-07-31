import numpy as np
import cv2

img = cv2.imread('img/GOAT.jpg', 0)
img = cv2.resize(img, (0, 0), fx=0.6, fy=0.6)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('img/GOAT2.jpg', img)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
