import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
(h, s, v) = cv2.split(img)
img2 = cv2.imread('equalized_v.png',0)
img1 = img2.astype(np.uint8)
merged = cv2.merge([h,s,img1])
merged = cv2.cvtColor(merged,cv2.COLOR_HSV2BGR)
cv2.imwrite('v1.png',merged)