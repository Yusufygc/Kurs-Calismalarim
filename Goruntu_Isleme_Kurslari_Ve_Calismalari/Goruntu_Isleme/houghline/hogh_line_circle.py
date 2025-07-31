import cv2
import numpy as np

img1 =cv2.imread("C:\\Users\\TUF Dash F15\\Desktop\\KODLAR\\IMAGE_PROCESSING\\Goruntu_Isleme\\klasor10\\coins.jpg")
img2 =cv2.imread("C:\\Users\\TUF Dash F15\\Desktop\\KODLAR\\IMAGE_PROCESSING\\Goruntu_Isleme\\klasor10\\balls.jpg")

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 =cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray1,5)
img2_blur = cv2.medianBlur(gray2,5)


circles= cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1 =200, param2 =10,minRadius=15,maxRadius=90) # 1 değeri çözünürlük oranı sondaki şey circle arası 
# mesafeler yani çember bulacak parametreler ise methoda özeldir direkt girememiz gerekiyor. ilki gradian değeri 
# ikinci threshold değeri algılanan çember sayısına etki ediyorlar.
 
if circles is not None:
    circles = np.uint16(np.around(circles)) # tuttuğu aralığı ayarlamayı sağlıyor np.uint8,16 falan

    for i in circles[0,:]: # tuttuğu değerler tek tek incelenir
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2) #  i0,i1 çemberin merkezinin x ve y değeri i2 de yarıçap



# topların hepsini gösteremiyor çünkü göremiyor:) 
circles1= cv2.HoughCircles(img2_blur,cv2.HOUGH_GRADIENT,1,img2.shape[0]/8,param1 =200, param2 =10,minRadius=5,maxRadius=60) 

 
if circles1 is not None:
    circles1 = np.uint16(np.around(circles1)) 

    for i in circles1[0,:]: 
        cv2.circle(img2,(i[0],i[1]),i[2],(0,255,0),2) 





cv2.imshow("img",img1)
cv2.imshow("img2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


