import cv2
import numpy as np 

cap = cv2.VideoCapture("C:\\vscode\\Teknofest\\klasor9\\dog.mp4")

while 1:
    _,frame =cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # beyaz renkler için olan hsv aralığı belirtmemiz gerekiyor.
    tolerans = 15
    lower_white = np.array([0,0,255-tolerans])
    upper_white = np.array([255,tolerans,255])

    mask = cv2.inRange(hsv,lower_white,upper_white) # hsv ye çevirdiğimiz değerlerin(frame) içinde belirttiğimiz max min aralığı dışındakileri sil yani maskele
    res = cv2.bitwise_and(frame,frame, mask = mask) # önce videonun kendisi sonra kazınmış hali gelsin diye ikişer ikişer yazdık özel kullanım

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("reseult",res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()














