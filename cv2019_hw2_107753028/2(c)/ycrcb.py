import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
ycrcb = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
(y, cr, cb) = cv2.split(ycrcb)
eq_V = cv2.equalizeHist(y)
img1 = eq_V.astype(np.uint8)
merged1 = cv2.merge([img1,cr,cb])
merged = cv2.cvtColor(merged1,cv2.COLOR_YCrCb2RGB)
cv2.imwrite('y2.png',merged)