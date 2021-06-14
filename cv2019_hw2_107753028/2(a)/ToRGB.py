import cv2
img = cv2.imread('mp2a.jpg')
(b, g, r) = cv2.split(img)
cv2.imwrite('r.jpg', r)

