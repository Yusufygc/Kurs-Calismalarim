import cv2
import numpy as np


font = cv2.FONT_HERSHEY_SIMPLEX

font1 = cv2.FONT_HERSHEY_COMPLEX



img =cv2.imread("C:\\vscode\\Teknofest\\klasor11\\polygons.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

conturs,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in conturs :
    epsilon =0.01*cv2.arcLength(cnt,True) # ktrue şekil kaplı mı değil mi onun için
    approx =cv2.approxPolyDP(cnt,epsilon,True) 
    cv2.drawContours(img,[approx],0,(0),5)

    x = approx.ravel()[0] # tüm sütunları satıra döker
    y = approx.ravel()[1]

    
    if len(approx) == 3:
        cv2.putText(img,"Ucgen",(x,y),font,1,(0))
    
    elif len(approx) ==4:
        cv2.putText(img,"DORTGEN",(x,y),font,1,(0))
    
    elif len(approx) == 5:
        cv2.putText(img,"Besgen",(x,y),font,1,(0))

    elif len(approx) == 6:
        cv2.putText(img,"altigen",(x,y),font,1,(0))

    else :
        cv2.putText(img,"elips",(x,y),font,1,(0))


cv2.imshow("img",img)

cv2.waitKey(0)

cv2.destroyAllWindows()