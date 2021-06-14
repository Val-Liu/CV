import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)
cv2.imwrite('v.jpg', v)
