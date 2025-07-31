import cv2


vid = cv2.VideoCapture("C:\\vscode\\Python\\Teknofest\\haarCascadeUyg\\test_videos\\smile.mp4")

face_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\frontalface.xml")
# yandan bakan inasnların suratı kolay kolay algılayamıyor

smile_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\smile.xml")




while 1 :
    ret,frame =vid.read()
    frame = cv2.resize(frame,(840,480))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,7)
    
    for (x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x + w , y + h),(0,0,255),2)

    roi_frame = frame[y: y+h , x: x+w]

    roi_gray = gray[y: y+h , x: x+w]

    smiles= smile_cascade.detectMultiScale(roi_gray,1.5,5)

    for (sx,sy,sw,sh) in smiles :
        cv2.rectangle(roi_frame,(sx,sy),(sx + sw , sy + sh),(0,0,255),2)

    cv2.imshow("img",frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):  
        break

vid.release()
cv2.destroyAllWindows()