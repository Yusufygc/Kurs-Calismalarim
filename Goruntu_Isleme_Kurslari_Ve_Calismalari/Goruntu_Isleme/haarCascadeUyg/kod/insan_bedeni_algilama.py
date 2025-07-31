import cv2 

# haar-like algortiması insan ve araç tespit etmede çok başarılı değildir çünkü bunlar çooook çeşitlidirler.

img =cv2.imread("C:\\vscode\\Python\\Teknofest\\haarCascadeUyg\\test_images\\body.jpg")

body_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\fullbody.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bodies = body_cascade.detectMultiScale(gray,1.1,3)

for (x,y,w,h) in bodies :
        cv2.rectangle(img,(x,y),(x + w , y + h),(0,0,255),2)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

