import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)
#cv2.imwrite('v.jpg', V)

eq_V = cv2.equalizeHist(v)
#img2 = cv2.imread('equalized_v.png',0)
img1 = eq_V.astype(np.uint8)
merged = cv2.merge([h,s,img1])
#merged = cv2.cvtColor(merged,cv2.COLOR_HSV2BGR)
cv2.imwrite('v2.png',merged)