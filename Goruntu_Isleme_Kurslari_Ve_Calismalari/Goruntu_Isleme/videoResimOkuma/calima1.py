import cv2

img = cv2.imread("klon.jpg",) # gri istersen cv2.IMREAD_GRAYSCALE ya da 0 yazarız

#print(img) # matrisleri gördük

#cv2.namedWindow("image",cv2.WINDOW_NORMAL)# açtığımız pencereyi manuel olarak boyutlandırmamaız sağlar
cv2.imshow("image",img) # çalışma esanasında hangi adla çalışacağız ve kaynağını belirtiyoruz

cv2.imwrite("klon1.jpg", img)

cv2.waitKey()
cv2.destroyAllWindows()





