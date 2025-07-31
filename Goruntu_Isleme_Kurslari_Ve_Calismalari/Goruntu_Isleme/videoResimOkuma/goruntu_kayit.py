import cv2


cap = cv2.VideoCapture(0)

fileName = "C:\Spyder\Teknofest\webcam.avi"

codec = cv2.VideoWriter_fourcc('w', 'm', 'v', '2')

frameRate = 30

resolution = (640,480)


videoFileOutput = cv2.VideoWriter(fileName,codec ,frameRate , resolution)


while True:
    ret, frame = cap.read()
    frame =cv2.flip(frame,1)
    videoFileOutput.write(frame)


    cv2.imshow("webcam live",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    
videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()

