# elimizdeki bir şablonu resimde var mı yok mu diye kontrol etmemizi sağlar

import cv2

import numpy as np

image_path = "C:\\vscode\\Teknofest\\klasor12\\starwars.jpg"

template_path = "C:\\vscode\\Teknofest\\klasor12\\starwars2.jpg"  # şablon demek



img =cv2.imread(image_path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


temp =cv2.imread(template_path,0) 
w,h =temp.shape[::-1]
 
# print(temp.shape) # eğer renkliyse kanal sayısı da gözükecek değilse sadece boyutlar ----> (117, 121) yani gri imiş
# gray1 = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)


# bu fonksiyon şablonu resimdeki uygun yere yaerleştirecek
result = cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED) # bundaki değerler bire ne kadar yakın olursa şablonun yerleştirileceği yer de o kadar doğru olur
#print( result)
location = np.where(result >= 0.9) # en doğru değer için 0.7 değerini yükselttik
# print(location)
for point in zip(*location[::-1]): # genişlik ve yükseklik alıyor ama -1 olunca tam tersi
    cv2.rectangle(img,point,(point[0] + w , point[1] + h) ,(0,0,255),3)
    #print(point)

cv2.imshow("img" ,img)
#cv2.imshow("temp" ,temp)
#cv2.imshow("result" ,result)
cv2.waitKey(0)
cv2.destroyAllWindows()
