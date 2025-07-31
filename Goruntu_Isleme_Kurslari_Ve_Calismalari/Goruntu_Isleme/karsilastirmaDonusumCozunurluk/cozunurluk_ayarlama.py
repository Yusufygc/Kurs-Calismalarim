import cv2

windowName = " Live Video"

cv2.namedWindow(windowName)

cap = cv2.VideoCapture(0)

print("width = " + str(cap.get(3)))
print("height = " + str(cap.get(4)))

cap.set(3,1280) # önce değiştirmek istediğimiz eksen yani yatay olan diğeri dde çözünürlük
cap.set(4,720) 

print("width* = " + str(cap.get(3)))
print("height* = " + str(cap.get(4)))

while 1:
    ret , frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow(windowName,frame)

    if cv2.waitKey(1) == 27 : # esc ile çıkış
        break 

cap.release()
cv2.destroyAllWindows()