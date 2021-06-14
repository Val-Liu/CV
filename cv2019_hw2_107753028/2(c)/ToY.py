import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
ycrcb = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
(y, cr, cb) = cv2.split(ycrcb)
cv2.imwrite('y.jpg', y)

