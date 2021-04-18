import cv2 as cv
import sys

img = cv.imread('/home/pi/Pictures/crewdragon.jpg')

if img is None:
 sys.exit("The image could not be read.")
cv.imshow("OpenCV Image", img)
cv.waitKey(0)
cv.destroyAllWindows()