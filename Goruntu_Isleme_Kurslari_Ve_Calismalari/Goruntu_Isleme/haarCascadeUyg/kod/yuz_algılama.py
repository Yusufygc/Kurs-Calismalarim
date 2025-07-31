import cv2

img = cv2.imread("C:\\Users\\TUF Dash F15\\Desktop\\IMAGE_PROCESSING\\Goruntu_Isleme\\haarCascadeUyg\\test_images\\resmim2.jpg")

face_cascade = cv2.CascadeClassifier("C:\\Users\\TUF Dash F15\\Desktop\\IMAGE_PROCESSING\\Goruntu_Isleme\\haarCascadeUyg\\haarCascade\\frontalface.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray,1.3,7) # bu arkadaş resimlerdeki yüzlerin koordinatlarını bulmamızı sağlar
                                                 # 1.3 değeri ölçeklendirmedir resmi ne kadar küçülteceğimiz hakkında
                                                 # 4 ise belli bir bölgede en az 4 pencere yüz bulsun ki orada yüz olduğuna emin olalım
                                                 # yüzlerin korrdonitarini bulup tuple şeklinde saklayacak
                                                 # faces ın 4 değişkeni vardır yüzün sol üst köşesinin koordinatları ve genişlik ile yükseklik
            #### ilk başta 4 değişkeni verdik bu yüzden boyun kısmında da yüz buldu o yüzden 7 yaptık ki en az 7 pencere yüz bulurrsa emin olacağız 


for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x + w , y + h),(0,0,255),2)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
