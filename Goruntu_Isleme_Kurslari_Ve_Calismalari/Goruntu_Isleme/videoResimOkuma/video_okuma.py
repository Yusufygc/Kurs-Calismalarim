import cv2

cap = cv2.VideoCapture("antalya.mp4")

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame ,1) # if ret == 0: break yaparakta videoyu kapatabiliriz

    cv2.imshow("antalya",frame)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



