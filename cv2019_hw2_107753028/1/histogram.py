#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function
import sys
import os
import cv2
import numpy as np

def hist_eq(img):
    data = img.copy().flatten()
    hist, bins = np.histogram(data, 256, density=True)
    cdf = hist.cumsum()
    cdf = 255*cdf/cdf[-1]
    img_eq = np.interp(data, bins[:-1], cdf)
    return img_eq.reshape(img.shape)

def main(argv):
    if len(argv) < 2:
        print("usage: {} IMAGE".format(argv[0]))
        return 1
    image_path = argv[1]
    image_name, _ = os.path.splitext(os.path.basename(image_path))
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_eq = hist_eq(img)
    if not cv2.imwrite("equalized_{}.png".format(image_name), img_eq):
        return 1
    return 0

if __name__ == "__main__":
    main(sys.argv)