import cv2
import numpy as np

vid = cv2.VideoCapture("C:\\vscode\\Python\\Teknofest\\klasor22\\traffic.avi")

backsub =cv2.createBackgroundSubtractorMOG2()

sayac = 0

while True:
    ret,frame = vid.read()
    if ret : # ret true ise bloğa gir
        fgmask = backsub.apply(frame) #( arka planı çıkarma işlemi
        cv2.line(frame,(50,0),(50,300),(255,0,0),2)
        cv2.line(frame,(70,0),(70,300),(255,0,0),2)

        contours,hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try : hierarchy = hierarchy[0]
        except: hierarchy=[]

        for contur,hier in zip(contours,hierarchy): # çok fazla ve farklı değerler aldığı için zipledik ki daha rahat döndürsün
            (x,y,w,h)=cv2.boundingRect(contur) # çekilen koordinatları bu değiişkenlere atar
            if w >40 and h> 40:
                cv2.rectangle(frame,(x,y),(x + w , y+ h),(0,0,255),2)
                if x > 50 and x < 70 :
                    sayac +=1

        cv2.putText(frame,"car"+ str(sayac),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2,cv2.LINE_AA)

        cv2.imshow("CAr counter : ",frame)
        cv2.imshow("fgmask",fgmask)


        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

vid.release()
cv2.destroyAllWindows()


