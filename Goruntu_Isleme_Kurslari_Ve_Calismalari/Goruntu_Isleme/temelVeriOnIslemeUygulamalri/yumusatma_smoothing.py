import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")



blur = cv2.blur(img_filter,(5,5)) # kernel da sadece pozitif tek sayılar olmalı
gaussian_blur = cv2.GaussianBlur(img_filter,(5,5), cv2.BORDER_DEFAULT)
median_blur = cv2.medianBlur(img_median, 5) # pozitif tek sayı olmalı
bilateral_blur = cv2.bilateralFilter(img_bilateral, 9,95, 95)
 
# cv2.imshow("blur",blur)
# cv2.imshow("original",img_filter)
# cv2.imshow("GaussianBlur",gaussian_blur)
# cv2.imshow("median_blur",median_blur)
cv2.imshow("bilateral_blur",bilateral_blur)
cv2.imshow("img_bilateral",img_bilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()