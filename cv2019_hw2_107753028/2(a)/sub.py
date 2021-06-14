import cv2
img1 = cv2.imread('r3.png')
img2 = cv2.imread('r31.png')
cv2.imwrite('sub2.jpg',img1-img2)