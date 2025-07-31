import cv2 
import numpy as np


canvas = np.zeros((512,512,3), np.uint8) +255


font1 = cv2.FONT_HERSHEY_COMPLEX # font yazınca ide öneriyor zaten

font2 = cv2.FONT_ITALIC

cv2.putText(canvas, "python", (20,250) ,font2, 3 , (0,0,0) , cv2.LINE_AA)
cv2.putText(canvas, "openCV", (80,350) ,font2, 3 , (0,0,0) , cv2.LINE_AA)
# 3.sol alt köşedeki başlangıç kordinatı ,sonuncu yazının tipini belirliyor



cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
