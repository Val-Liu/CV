import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
(b, g, r) = cv2.split(img)
cv2.imwrite('b.jpg', b)