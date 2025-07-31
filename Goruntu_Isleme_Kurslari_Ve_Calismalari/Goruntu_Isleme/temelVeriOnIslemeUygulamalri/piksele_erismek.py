import cv2
import numpy as np


img = cv2.imread("klon.jpg")

boyut = img.shape
print(boyut)

color = img[420,500] # pikseldeki bgr değerlerine ulaşmak
print(color)


blue = img[420,500,0]# pikseldeki blue değerine ulaşmak
print(blue)

green =img[420,500,1]
print(green)


img[420,500,0] = 250 # piksledeki mavi değeri değiştirmek
print("yeni mavi",img[420,500,0])

blue1 = img.item(150,200,0) # 150 ye 200 deki mavi değerini blue1 e eşitlemek
print (blue1)

img.itemset((150,200,0), 172) # pikselein değerini değiştiriyoruz blue1 in değil
print("new blue1 :", img[150,200,0])


cv2.imshow("klon asker",img)
cv2.waitKey(0)
cv2.destroyAllWindows()








