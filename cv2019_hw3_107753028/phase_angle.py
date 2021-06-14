import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('3.jpg',0) 
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#ph_f = np.angle(f)
ph_fshift = np.angle(fshift)

plt.subplot(121),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(122),plt.imshow(ph_fshift,'gray'),plt.title('phase_angle')
plt.show()