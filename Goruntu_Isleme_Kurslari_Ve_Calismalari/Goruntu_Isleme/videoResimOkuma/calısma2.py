# PENCERELERİ YENİDEN BOYUTLANDIRMA
import cv2

cv2.namedWindow("klon") # mouse ile boyutlandırmamı<ı sağlar

img = cv2.imread("klon.jpg")

img = cv2.resize(img,(640,480)) # burada ise daha detaylı ve istediğimiz boyutlandırabiliriz


cv2.imshow("klon",img)

cv2.waitKey()
cv2.destroyAllWindows()

