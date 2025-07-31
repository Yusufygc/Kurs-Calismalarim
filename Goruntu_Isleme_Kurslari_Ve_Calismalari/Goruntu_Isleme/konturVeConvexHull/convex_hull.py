# dış bukey örtü

#####################  bu kod çalışmıyor ama ada_convex_hull.py çalışıyor burda açıklamalaar var ############
import cv2
import numpy as np

img =cv2.imread("C:\\vscode\\Teknofest\\klasor9\\map.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray,(3,3))

ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY) # min ve max thresh değerleri ile  oynarak resimdeki deformeleri en az inidrebiliriz
# 75 değeri fazla deorme ettiği için 50 ye çektik , gene oldu o yüzden 40 

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False)) # false değerin bulunduğu indisi döndürmeye yarıyor

backgraund = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8) # ilki threshin tutulduğu boyutun ilk depeğerini dondurur

for i in len(contours): # hull pointleri birleştirecez
    cv2.drawContours(backgraund,contours,i,(255,0,0),3,8,hierarchy) # 8 --> kesintisiz çizmeyi sağlıyor i ise indisler --> bu konturu çizcek
    cv2.drawContours(backgraund,hull,i,(0,255,0),1,8) #  bu da dış çizgiyi yani örtüyü


cv2.imshow("image",backgraund)

"""
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)
"""
cv2.waitKey(0)
cv2.destroyAllWindows()
















