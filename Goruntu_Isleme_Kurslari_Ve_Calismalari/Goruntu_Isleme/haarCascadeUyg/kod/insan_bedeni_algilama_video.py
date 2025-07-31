import cv2

vid = cv2.VideoCapture("C:\\vscode\\Python\\Teknofest\\haarCascadeUyg\\test_videos\\body.mp4")

body_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\fullbody.xml")

while 1 :
    ret,frame =vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray,1.09,4)
    
    for (x,y,w,h) in bodies :
        cv2.rectangle(frame,(x,y),(x + w , y + h),(0,0,255),2)

    cv2.imshow("video",frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):  
        break


vid.release()
cv2.destroyAllWindows()


# bodies = body_cascade.detectMultiScale(gray,1.1,3)



