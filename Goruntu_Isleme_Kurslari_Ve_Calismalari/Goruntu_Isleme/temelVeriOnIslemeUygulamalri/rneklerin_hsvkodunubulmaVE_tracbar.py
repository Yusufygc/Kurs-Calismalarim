import cv2
import numpy as np

cap =cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("trackbar")

cv2.resizeWindow("trackbar",500,500)


cv2.createTrackbar("lower - h", "trackbar", 0, 180, nothing)
cv2.createTrackbar("lower - s", "trackbar", 0, 255, nothing)
cv2.createTrackbar("lower - v", "trackbar", 0, 255, nothing)

cv2.createTrackbar("upper - h", "trackbar", 0, 180, nothing)
cv2.createTrackbar("upper - s", "trackbar", 0, 255, nothing)
cv2.createTrackbar("upper - v", "trackbar", 0, 255, nothing)


cv2.setTrackbarPos("upper - h", "trackbar", 180)
cv2.setTrackbarPos("upper - s", "trackbar", 255)
cv2.setTrackbarPos("upper - v", "trackbar", 255)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame , 1)
    
    frame_hsv = cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("lower - h", "trackbar")
    lower_s = cv2.getTrackbarPos("lower - s", "trackbar")
    lower_v = cv2.getTrackbarPos("lower - v", "trackbar")

    upper_h = cv2.getTrackbarPos("upper - h", "trackbar")
    upper_s = cv2.getTrackbarPos("upper - s", "trackbar")
    upper_v = cv2.getTrackbarPos("upper - v", "trackbar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

    cv2.imshow("original",frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



