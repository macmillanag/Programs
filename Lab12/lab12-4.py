import cv2 as cv
import numpy as np
img = cv.imread('me.jpg')
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
cv.imwrite("canny.jpg", cv.Canny(res, 200, 300)) # Canny in one line!
cv.imshow("canny", cv.imread("canny.jpg"))
cv.waitKey()
cv.destroyAllWindows()