# roi ----> region of interest ilgi alanı 

import cv2

img =cv2.imread ("klon.jpg")

roi = img[30:200 , 200:400] # önce dikey eksen sonra yatay eksen




cv2.imshow("kafa",roi)
cv2.imshow("resim",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
