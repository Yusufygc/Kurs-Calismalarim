import cv2

vid = cv2.VideoCapture("C:\\vscode\\Python\\Teknofest\\haarCascadeUyg\\test_videos\\faces.mp4")

face_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\frontalface.xml")

while 1 :
    ret,frame =vid.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,4)

    for (x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x + w , y + h),(0,0,255),2)

    cv2.imshow("img",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):  
        break

vid.release()
cv2.destroyAllWindows()

















