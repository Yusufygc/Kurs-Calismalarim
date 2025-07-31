import cv2 
import numpy as np

img = cv2.imread("atak.jpg",0)

row , col = img.shape # satır , sütün

M = np.float32([[1,0,50],[0,1,100]]) #• transformasyon yani dönüşüm matrisi
# matristeki 50 ve 100 değeri resimdeki siyah bölgeleri temsil ediyor yani o siyah bölgler kadar kaydırma yapılıyor

dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("dst", dst)
# print(row)
# print(col)

cv2.imshow("atak", img)
cv2.waitKey(0)
cv2.destroyAllWindows()