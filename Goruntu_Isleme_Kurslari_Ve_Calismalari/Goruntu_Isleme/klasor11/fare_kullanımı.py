import cv2

cap = cv2.VideoCapture("C:\\vscode\\Teknofest\\klasor11\\car.mp4")


circles = []
def mouse(event,x,y,lags,params): # event maosue haerketi x y oluşacak çemberin merkezi
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",mouse) # frame üzerine yapılan işleri belirtir.

while 1 :
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))

    for center in circles:
        cv2.circle(frame,center,20,(255,0,0),-1)

    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord("h"): # ekranı temizlememk için
        circles = []


cap.release()
cv2.destroyAllWindows()



















