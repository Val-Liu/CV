import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
(y, cr, cb) = cv2.split(img)
img = cv2.imread('equalized_y.png',0)
img1 = img.astype(np.uint8)
merged1 = cv2.merge([img1,cr,cb])
#merged = cv2.cvtColor(merged1,cv2.COLOR_YCrCb2RGB)
cv2.imwrite('y1.png',merged1)