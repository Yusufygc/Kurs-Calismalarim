import cv2
import numpy as np


img = cv2.imread("C:\\vscode\\Teknofest\\klasor8\\text.png")
img1 = cv2.imread("C:\\vscode\\Teknofest\\klasor8\\contour.png")

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)


corners = cv2.goodFeaturesToTrack(gray,50,0.01,10) # 50 max köşe sayısı ,0.01 kalite bilimsel kabulmuş , 10 da köseler  arası mesafe

corners = np.int0( corners)

for corner in corners:
    x , y = corner.ravel()
    cv2.circle(img1,(x,y),3,(0,0,255),-1)


cv2.imshow("corner",img1)
#cv2.imshow("ujgen",img1)


cv2.waitKey(0)
cv2.destroyAllWindows()




















