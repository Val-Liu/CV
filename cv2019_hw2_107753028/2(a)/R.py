import cv2
import numpy as np
img = cv2.imread('mp2a.jpg')
(b, g, r) = cv2.split(img)
img = cv2.equalizeHist(g)
img1 = img.astype(np.uint8)
merged = cv2.merge([b,img1,r])
cv2.imwrite('r31.png',merged)