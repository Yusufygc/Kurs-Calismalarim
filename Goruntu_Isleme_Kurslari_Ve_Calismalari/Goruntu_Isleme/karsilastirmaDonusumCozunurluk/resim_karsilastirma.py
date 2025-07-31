import cv2
import numpy as np
# İKİ RESMİN BİRBİRİNE EŞİT OLMASI DEMEK PİKSELLERİ VE RENKLERİNİN EŞİT OLMASI DEMEKTİR

path1 = "C:\\vscode\\Teknofest\\klasor12\\aircraft.jpg"
path2 = "C:\\vscode\\Teknofest\\klasor12\\aircraft1.jpg"

img1 = cv2.imread(path1)
img1 = cv2.resize(img1,(650,580))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(650,580))

img3 = cv2.medianBlur(img1,7)  


if img1.shape == img3.shape:
    print("aynı boyuttalar")
else:
    print("aynı boyutta değiller.")

"""
if img1.shape == img2.shape:
    print("aynı boyuttalar")
else:
    print("aynı boyutta değiller.")

difference = cv2.subtract(img1,img2) # İKİ RESMİ KARŞILAŞTIRIP FARKLI OLAN YERLERİN RENGİNİ DEĞİŞTİRİR.
"""
difference = cv2.subtract(img1,img3)

b,g,r = cv2.split(difference)

# cv2.countNonZero(b) # içerisinie girline değişkenin tuttuğu değerleri tek tek tarar ve kaç tane sıfır olmadığına bakar

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) and cv2.countNonZero(r) :
    print("Tamamen eşit.")
else:
    print("tamamen eşit değil.")

cv2.imshow("difference",difference) # BİZİM RESİMLER AYNI OLDUĞU İÇİN HERHANGİ BİR BOYAMA OLMADI
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
















