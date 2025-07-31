import cv2
import numpy as np
from matplotlib import pyplot as plt

# kendi oluşturduğumuz tuvalde böyle oluyor bir de aşağıda normal resim deneyeceğiz
"""
img = np.zeros((500,500),np.uint8) + 50 # + ....herhangi bir değer ekleyerek sadce sıfırlardan oluşmasını engelleriz daha doğrsu değiştirebiliriz

cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
cv2.rectangle(img,(200,150),(0,60),(255,255,255),-1)

plt.hist(img.ravel(),256,[0,256]) # ravel bütün piksle değerlerini tek satır da toplar, 2. si kaç deper oldğu ,3.sü değer aralığı
plt.show()
"""
resim = cv2.imread("C:\\vscode\\Teknofest\\klasor8\\smile.jpg")

b,g,r = cv2.split(resim)


cv2.imshow("smile",resim)
plt.hist(resim.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()






















