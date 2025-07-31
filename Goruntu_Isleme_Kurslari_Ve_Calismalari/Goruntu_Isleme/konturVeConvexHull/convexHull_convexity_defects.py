import cv2

img =cv2.imread("C:\\vscode\\Teknofest\\klasor9\\star.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh =cv2.threshold(gray, 127,255,0) #hata olduğu için cv2.THRESH_BINARY bunu kaldırıp 0 koyduk

contours,_ = cv2.findContours(thresh,2,1)#hata olduğu için cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE bunu kaldırıp 2,1 koyduk


cnt = contours[0]

hull = cv2.convexHull(cnt,returnPoints=False)

defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
     
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,255,0],-1)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# s,e,f,d = defects[i,0] #s yıldızın uç noktaları e end point f en uzak nokta  d mesefa