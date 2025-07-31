import cv2


img =cv2.imread("C:\\vscode\\Teknofest\\klasor9\\ucgen.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh =  cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

M = cv2.moments(thresh) # M = moments

#print(M) # sözlük biçiminde tutuyor

X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])

cv2.circle(img,(X,Y), 5,(0,0,0),-1) # ağırlık merkezini yukarda bulduk burda işaretliyoruz


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





























































