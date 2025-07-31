import cv2


vid = cv2.VideoCapture("C:\\vscode\\Teknofest\\klasor11\\eye_motion.mp4")


while 1:
    ret,frame = vid.read()
    if ret is False :
        break

    roi = frame[80:210,230:450]    
    rows,cols,_ = roi.shape
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    _,threshold = cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV) 
    # THRESH_BINARY_INV bunu kullandık çünkü siyah olanları beyaz yapmak istiyoruk
    # istemediğimiz yerler de beyaz olduğu için alt değeri biraz daha düşürdük 50-->30 -->3

    contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours , key = lambda x: cv2.contourArea(x),reverse=True) #contur değerleri bu fonksiyona göre sıralanacak

    # direkt göz bebğine odaklandığımız için en büyük alan ona ait reverse=True bunulada en sondan sıralattık bu yüzden direkt istediğimie ulaşabiliriz

    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt) #dikdörtgenin sol üst ve sağ alt değerlerini çekip atamayı sağladık
        cv2.rectangle(roi, (x,y) , (x + w , y + h),(0,0,255),2)
        cv2.line(roi, (x + int(w/2) , 0), (x + int(w/2) , rows), (0,255,0), 2)
        cv2.line(roi, (0 , y+ int(h/2)), (cols, y + int(w/2)), (255,0,0), 2)
        break
 
   # frame[80:210,230:450] = roi # tüm videoda görmeyi sağlar    

    # cv2.imshow("frame",frame)

    cv2.imshow("roi",roi)

    cv2.imshow("thresh roi",threshold)

    if cv2.waitKey(80) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()















