import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    roi = frame[50:250,200:400] # alan seçiyoruz ilki y ikincisi x değeri y1 = 50 y2 = 250 , x1 = 250 ,x2 = 450 [y1:y2,x1:x2]
    cv2.rectangle(frame,(200,50),(400,250),(0,0,255),2) # ikincisi (x1,y1) ,üçüncüsü (x2,y2)


    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,45,79],dtype=np.uint8)
    upper_color = np.array([17,255,255],dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_color,upper_color)

    kernel =np.ones((3,3),np.uint8) #beyaz zemin üzerindeki siyah karıncalanmaları yk etmek istediğimiz için birlerden oluşan bir kernel yaptık
    mask =cv2.dilate(mask,kernel,iterations=1)

    mask = cv2.medianBlur(mask,15)

    #cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()