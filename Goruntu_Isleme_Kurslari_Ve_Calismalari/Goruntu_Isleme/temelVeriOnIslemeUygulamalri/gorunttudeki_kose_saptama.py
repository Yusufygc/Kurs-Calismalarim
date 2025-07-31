import cv2


cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # 1 y eksenidir

    edges = cv2.Canny(frame,100,200) ## 100,200 min ve max eşik değeri 

    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)


    if cv2.waitKey(5) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()


