import cv2
import numpy as np

img = cv2.imread("klon.jpg")

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("klon GRAY",img_gray)
cv2.imshow("klon hsv",img_hsv)
cv2.imshow("klon rgb",img_rgb)
cv2.imshow("klon",img)



cv2.waitKey(0)
cv2.destroyAllWindows()

















