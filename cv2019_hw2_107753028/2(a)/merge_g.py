import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
(b, g, r) = cv2.split(img)
img = cv2.imread('equalized_g.png',0)
img1 = img.astype(np.uint8)
#print r.shape
#print img1.shape
merged = cv2.merge([b,img1,r])
cv2.imwrite('r3.png',merged)