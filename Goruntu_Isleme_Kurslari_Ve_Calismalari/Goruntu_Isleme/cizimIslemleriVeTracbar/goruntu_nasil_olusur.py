import numpy as np
import cv2

img = np.zeros((10,10,3), dtype = np.uint8) # 3.değeri yani kanalları kaldırırsak siyah beyza görüntü elde ederiz


img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,155)
img[0,3] = (255,255,25)
img[1,0] = (155,255,255)
img[2,0] = (55,255,255)
img[3,0] = (255,205,255)
img[4,0] = (55,25,25)
img[5,5] = (255,255,255)


""" # siyah beyaz görüntü
img = np.zeros((10,10), dtype = np.uint8)
img[0,0] = 255
img[0,1] = 200
img[0,2] = 155
img[0,3] = 25
img[1,0] = 155
img[2,0] = 55
img[3,0] = 205
img[4,0] = 55
"""

img = cv2.resize(img ,(1000,1000) , interpolation = cv2.INTER_AREA)# sondaki şey çakışmaları engellemek için




cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

