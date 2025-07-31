import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype = np.uint8) +255

#canvas = np.ones((515,512,3) , dtype = np.uint8) 



cv2.line(canvas , (50,50),(512,512),(255,0,0), thickness = 5) # bas,t çizgi

# nereye çiizm yapılacağı, nerden başlayacak , nerde bitecek ,renk, kalınlık

cv2.line(canvas , (130,300),(275,375),(80,50,40), 7) # bas,t çizgi

#### dikdörtgen kare çizdirmece
cv2.rectangle(canvas, (100,100), (300,300), (0,255,0),3) 
# kalınlığı -1 yaparsan içini doldurur

cv2.rectangle(canvas, (400,400), (250,200), (0,255,0),-1)

#### daire çizdirmece

cv2.circle(canvas,(175,243),80,(0,0,255),15)
# kalınlığı -1 yaparsan içini doldurur


#### üçgen (amma elle yapacağik özel func yok)

cv2.line(canvas , (50,50),(50,480),(255,0,0), thickness = 5)

cv2.line(canvas , (50,50),(375,250),(255,0,0), thickness = 5)

cv2.line(canvas , (50,480),(375,250),(255,0,0), thickness = 5)


# bbu arkadaş pek tatlı kordinatları girerek kapalı veya açık şekil oluşturabiliriz

points = np.array([[[112,155] , [238,382] , [400,215]]], np.int32) #  , [156,325] bunu ekleyeip veya daha fazlasını çoğalabilriz

cv2.polylines(canvas, [points], True, (200,20,0),5) # True or False describe to line or figure




cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()




