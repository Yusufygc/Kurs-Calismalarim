import cv2
import numpy as np

def findMaxCounter(contours):
    max_i = 0 # max alanın tutulduğu indis
    max_area = 0

    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])
 
        if max_area < area_face:
            max_area = area_face
            max_i = i
        try:
            c = contours[max_i]

        except:
            contours = [0]
            c = contours = [0]

        return c
    


cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    roi = frame[50:250,200:400] # alan seçiyoruz ilki y ikincisi x değeri y1 = 50 y2 = 250 , x1 = 250 ,x2 = 450 [y1:y2,x1:x2]
    cv2.rectangle(frame,(200,50),(400,250),(0,0,255),0) # ikincisi (x1,y1) ,üçüncüsü (x2,y2) kalınlığı 2 den 0 çeviriyoruz çünkü hsv mask işlemlerine dahil olup hataya sebep olacak


    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,45,79],dtype=np.uint8)
    upper_color = np.array([17,255,255],dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_color,upper_color)

    kernel =np.ones((3,3),np.uint8) #beyaz zemin üzerindeki siyah karıncalanmaları yk etmek istediğimiz için birlerden oluşan bir kernel yaptık
    mask =cv2.dilate(mask,kernel,iterations=1)
    mask = cv2.medianBlur(mask,15)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # yüzümüzün bulunduğu roi deki max konturu bulup ona göre işlem yapmka için çünkü karıncalanma falan da var orda    
           c = findMaxCounter(contours)
           enSol = tuple(c[c[:, :, 0].argmin()][0]) # en sol x in en küçük olduğu yer
           enSag = tuple(c[c[:, :, 0].argmax()][0]) # en sağ x in en büyük olduğu yer
           enUst = tuple(c[c[:, :, 1].argmin()][0]) # bundaki bir çünkü y yi temsil ediyor 0 ise x i temsil ediyor

           cv2.circle(roi,enSol,5,(0,255,0),2)
           cv2.circle(roi,enSag,5,(0,255,0),2)
           cv2.circle(roi,enUst,5,(0,255,0),2)

           cv2.line(roi,enSol,enUst,(0,255,0),2)
           cv2.line(roi,enUst,enSag,(0,255,0),2)

      

    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break




cap.release()
cv2.destroyAllWindows()