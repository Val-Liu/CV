import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
img = cv2.imread('3.jpg',0) 
f = np.fft.fft2(img) 
print(f) 
fshift = np.fft.fftshift(f) 
spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray') 
plt.title('Input Image'), plt.xticks([]), plt.yticks([]) 
plt.subplot(122),plt.imshow(spectrum, cmap = 'gray') 
plt.title('Spectrum'), plt.xticks([]), plt.yticks([]) 
plt.show() 