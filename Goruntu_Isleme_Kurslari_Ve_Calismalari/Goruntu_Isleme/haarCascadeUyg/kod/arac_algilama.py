import cv2

# YİNE TIRT 

img = cv2.imread("C:\\vscode\\Python\\Teknofest\\haarCascadeUyg\\test_images\\car.jpg")

car_cascade = cv2.CascadeClassifier("C:\\vscode\Python\\Teknofest\\haarCascadeUyg\\haarCascade\\car.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray,1.3,1)

for (x,y,w,h) in cars :
    cv2.rectangle(img,(x,y),(x + w , y + h),(0,0,255),2)

cv2.imshow("iamage",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
