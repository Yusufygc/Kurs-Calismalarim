import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3) , np.uint8)

cv2.namedWindow("image") # tekrar adlandırdık çünkü trackbar arayüzünü kullanacağımız resme yerleştirek / belirtmek için


# cv2.createTrackbar(trackbarName, windowName, value, count, onChange)

cv2.createTrackbar("R", "image", 0,255, nothing) # 0,255 renk aralığıdır , sondaki func ise trackbar func ın gerekliliğidir

cv2.createTrackbar("G", "image", 0,255, nothing)

cv2.createTrackbar("B", "image", 0,255, nothing)

switch = "0: OFF, 1: ON" # enaktar

cv2.createTrackbar(switch, "image", 0,1, nothing)


# pencerenin yanilenmesi için ve renk değişiminin sağlanabilmesi için
while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    # r = cv2.getTrackbarPos(trackbarname, winname)
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s =cv2.getTrackbarPos(switch, "image") # switch için
    
    
    if s == 0:
        img[:] = [0,0,0]
    if s == 1:
        img[:] = [b,g,r] # img deki bütün piksel değerlerindeki renklere erişmek ve onları üstetki değişkenlerle eşlemek için

    # switch i aktif etmezsek aşağıdakini kullanabiliriz
    # img[:] = [b,g,r] # img deki bütün piksel değerlerindeki renklere erişmek ve onları üstetki değişkenlerle eşlemek için
    

cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    