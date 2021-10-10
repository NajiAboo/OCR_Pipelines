import cv2 as cv
import numpy as np

img = cv.imread("lion.jpg")
#cv.imshow("img", img)
#cv.waitKey(0)

cvt_img =cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gr", cvt_img)
cv.waitKey(0)

