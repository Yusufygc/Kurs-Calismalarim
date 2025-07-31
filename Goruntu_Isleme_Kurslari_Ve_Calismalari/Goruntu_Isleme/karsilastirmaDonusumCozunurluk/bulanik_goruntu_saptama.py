import cv2

img =cv2.imread("C:\\vscode\\Teknofest\\klasor12\\starwars.jpg")

blur =cv2.medianBlur(img,7)

laplacian =cv2.Laplacian(blur,cv2.CV_64F).var() # resmin blurlu olup olmadığını kontrol eder.virgülden sonrası prosedür
laplacian1 =cv2.Laplacian(img,cv2.CV_64F).var()

# print(laplacian)  # blurlama arttıkça gösterdikleri değer azalır. 
# print(laplacian1) #bunlardan gelen değerlere göre karar yapıları oluşturup blurlu olup olmadığına bakacağız

if laplacian < 500:
    print("blurlu rsim")


"""
cv2.imshow("img",img) 
cv2.imshow("blur",blur) 
cv2.waitKey(0)
cv2.destroyAllWindows()
"""