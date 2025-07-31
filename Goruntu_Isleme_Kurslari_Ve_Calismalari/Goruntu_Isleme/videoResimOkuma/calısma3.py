
# EN BOY ORANI

import cv2

def resizewithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):# cv2.INTER_AREA BU ZIMBIRTI BOYUTLANDIRMA ESANSINDAKİ ÇAKIŞMALARI ENGELLER
    dimension =None
    
    (h,w) = img.shape[:2] # boy ve en 
    
    if width is None and height is None :
        return img

    
    if width is None:
        r = height / float(h)
        dimension = (int(w*r), height)

    else:
        r = width / float(w)
        dimension =(width , int(h*r))


    return cv2.resize(img, dimension, interpolation = inter)


img = cv2.imread("klon.jpg")

img1 =resizewithAspectRatio(img, width = None, height = 600, inter = cv2.INTER_AREA)

cv2.imshow("orjinal",img)
cv2.imshow("resized",img1)

cv2.waitKey()
cv2.destroyAllWindows()


