import cv2 
import  numpy as np

img = cv2.imread("atak.jpg",0)

kernel = np.ones((5,5),np.uint8) # kernel değerleri değişebilir

# dilation = cv2.dilate(img, kernel, iterations = 5) # kalınlaştırma beyazlıklar artıyor kalınlaşıyor 

# erozyon = cv2.erode(img, kernel, iterations = 1) # iteration = tekrar siyahlıklar artıyor inceliyor

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # gürültüler giderilmeye çalışılır

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # cisimdeki gürültüler giderilmeye çalışılır

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("tophat", tophat)
#cv2.imshow("gradient", gradient)
#cv2.imshow("closing", closing)
#cv2.imshow("opening", opening)
# cv2.imshow("dilation", dilation)
# cv2.imshow("erozyon", erozyon)

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
