import cv2 
import numpy as np

img = cv2.imread("atak.jpg",0)

row , col = img.shape # satır , sütün

#M = cv2.getRotationMatrix2D(center, angle, scale)

M = cv2.getRotationMatrix2D((col/3, row/3), 180, 1)

dst = cv2.warpAffine(img, M, (col, row))



cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
