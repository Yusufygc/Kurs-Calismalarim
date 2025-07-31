#nesne tespitinde önemli bir yer tutar

# yüksek doğruluklu kontur çizimleri için binary resimler kullanmalıyız : cv2.cvtColor(), cv2.thrrshold()
# kontur kordinatlarının tespiti : cv2.findConturs()
# bulunan noktaların çizimi : cv2.drawContours()

import cv2 

img = cv2.imread("C:\\vscode\\Teknofest\\klasor9\\contour.png")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # kullandığımız resim siyah beyaz olsada ne olur ne olmaz yine de çevirelim

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # _ işe yaramayan ama fonksiyonun kullanımı için yaptığımız bir şey

contours,_= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# koordinatlar # son iki parametre default olarka kullanılır hayta almamak için kullanıyoruz

#print(contours)

cv2.drawContours(img,contours,-1,(0,0,255),3) # -1 tüm kenarları yapıyor sıfır yaparsak sadece resmin çerçevesini yapar içine tokanmaz

cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




