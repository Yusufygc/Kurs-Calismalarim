import cv2

img = cv2.imread("C:\\vscode\\Python\\Teknofest\\haarCascadeUyg\\test_images\\eye.png")

face_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\frontalface.xml")

eye_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\eye.xml")


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,10)

for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x + w , y + h),(0,0,255),2)

img2 = img[y:y+h , x:x+w]

gray2 = gray[y:y+h , x:x+w]

eyes = eye_cascade.detectMultiScale(gray2,1.3,10)

for (ex,ey,ew,eh) in eyes :
    cv2.rectangle(img2,(ex,ey),(ex +ew , ey + eh),(255,0,0),2)

cv2.imshow("iamage",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




















