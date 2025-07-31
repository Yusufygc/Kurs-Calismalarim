import numpy as np
import cv2

canvas = np.zeros((512,512,3), dtype = np.uint8) + 255 # canvas = tuval 512x512 boyutunda 3 kanallı 
# +255 işlemi beyaz tuval elde etmek için
# print(canvas)



cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()