import cv2

def nothing(x):
    pass

img1 = cv2.imread( "C:\\vscode\\Teknofest\\klasor12\\aircraft.jpg")
img1 = cv2.resize(img1,(640,480))

img2 = cv2.imread("C:\\vscode\\Teknofest\\klasor12\\balls.jpg")
img2 = cv2.resize(img2,(640,480))

output =cv2.addWeighted(img1,0.5, img2,0.5,0)


WindowName = "Donusum programi"

cv2.namedWindow(WindowName)

cv2.createTrackbar("alpha-beta",WindowName,0,1000,nothing)

while 1:
    cv2.imshow(WindowName,output)

    alpha = cv2.getTrackbarPos("alpha-beta",WindowName) /1000 # çünkü değerler 0-1 arası değişiyordu 
    betha = 1 - alpha
    print("alpha : " ,alpha , " betha : " ,betha)
    
    output =cv2.addWeighted(img1,alpha, img2,betha,0)
  
    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()

