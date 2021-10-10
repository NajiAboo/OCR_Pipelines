import cv2 as cv

img = cv.imread("lion.jpg")

"""
Resize can be done using dsize or fx, fy
"""
print(img.shape)

out = cv.resize(img, (600,600))
print(out.shape)

out1 = cv.resize(img, None, fx=2, fy=2)
print(out1.shape)
