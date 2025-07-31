import cv2

img =cv2.imread("C:\\vscode\\Teknofest\\klasor9\\ucgen.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh =cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = (contours[0])

area =cv2.contourArea(cnt) # alan  buluyoruz

print(area)

M = cv2.moments(cnt) # bu şekildede alan bulabiliyoruz
print(M["m00"])

perimeter = cv2.arcLength(cnt,True) # çevre bulmak için true şekil kapalıysa devam etmek için
print(perimeter)

cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()

























