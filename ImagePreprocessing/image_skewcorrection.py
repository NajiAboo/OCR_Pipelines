"""
 Correct the rotation
 
 - Detect a feature and calculate the skew angle
 
 for example :
     
     1. Detect the box or a text 
     2. Find the skew angle (cv2.minAreaReact())
     3. it work between -45 to 45
     
     
"""

import cv2 as cv

# Read input image
img = cv.imread("deskew_box.PNG")
cv.imshow("skewed image", img)
#cv.waitKey(0)
#cv.destroyAllWindows()

"""
Steps
1. findCounters
2. Get the max counter
3. calculate the image angle
4. rotate the image based on the angle
"""

img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

#apply binary thresholding
ret, thresh = cv.threshold(img_gray,0,255, cv.THRESH_BINARY_INV+ cv.THRESH_OTSU )

#find contours
contours, _ = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#find the max region 
contours = sorted(contours,key=cv.contourArea,reverse=True)
max_cnt = contours[0]

angle = cv.minAreaRect(max_cnt)[-1]
print(angle)
if angle < -45:
    angle = 90 + angle

if angle > 45:
    angle = angle - 90

print(angle)
    
# find the central point of the image to rotate
height, width,_ = img.shape
center = (width/2, height/2)

M = cv.getRotationMatrix2D(center=center, angle=-3, scale=1)

dst = cv.warpAffine(img, M, (width, height), flags=cv.INTER_LINEAR, borderMode=cv.BORDER_REPLICATE)
cv.imshow("oput", dst)
cv.waitKey(0)
cv.destroyAllWindows()












