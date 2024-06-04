from PIL import Image

im = Image.open('python.jpg')
print(im.size)

import numpy as np

im_pillow = np.asarray(im)
print(im_pillow.shape)

im_pillow_c0 = im_pillow[:, :, 0]
im_pillow_c1 = im_pillow[:, :, 1]
im_pillow_c2 = im_pillow[:, :, 2]

zeros = np.zeros((im_pillow.shape[0], im_pillow.shape[1], 2))
print(zeros.shape)

im_pillow_c1_1 = im_pillow_c1[:,:, np.newaxis]
print(im_pillow_c1_1.shape)
im_pillow_c1_1_cc = np.concatenate((im_pillow_c1_1, zeros), axis=2)
print(im_pillow_c1_1_cc.shape)

from matplotlib import pyplot as plot




import cv2

im_cv = cv2.imread("python.jpg")
type(im_cv)
print(im_cv.shape)
