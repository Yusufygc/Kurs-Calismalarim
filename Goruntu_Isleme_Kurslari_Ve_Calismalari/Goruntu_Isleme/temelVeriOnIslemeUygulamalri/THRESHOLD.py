import cv2 
import  numpy as np
from matplotlib import pyplot as plt

# resmimiz siyah beyaz halde olmalıdır treshold yapraken
 
img = cv2.imread("atak.jpg",0)

ret ,th1 = cv2.threshold(img,150,200,cv2.THRESH_BINARY) # ret -< return th1 <- treshold

th2 =cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)

th3 =cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

cv2.imshow("img-th1", th1)
cv2.imshow("img-th2", th2)
cv2.imshow("img-th3", th3)


# cv2.imshow("atak", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

 
