import cv2
import numpy as np

img =cv2.imread("C:\\Users\\TUF Dash F15\\Desktop\\KODLAR\\IMAGE_PROCESSING\\Goruntu_Isleme\\klasor10\\h_line.png")
#C:\Users\TUF Dash F15\Desktop\KODLAR\IMAGE_PROCESSING\Goruntu_Isleme\klasor10

gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,75,150) # köşe tespit edeceeğğeez



# cv2.HoughLines() # bu arkadaş cpu yu çok yorduğu için diğerini kullanmak daha mantıklı
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200) # 2 ve 3. standart sanırım sonuncu threshold değeri sonuncusu boşlukların dolmasını sağlıyor

#print(lines)

# bu line ları direkt çekemediğimiz için for döngüsü kurmmamız lazım

for line in lines:
    x1,y1 ,x2,y2 =line[0] # line ların başlangıç ve bitiş değerleri
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)



cv2.imshow("img",img)   
cv2.imshow("gary",gray)
cv2.imshow("canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()










