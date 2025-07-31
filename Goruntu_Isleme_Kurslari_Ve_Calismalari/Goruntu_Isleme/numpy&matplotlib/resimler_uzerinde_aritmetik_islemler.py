import matplotlib.pyplot as plt
import numpy as np

path = "C:\\vscode\\Python\\Teknofest\\numpy&matplotlib\\map.jpeg"
img = plt.imread(path)

plt.subplot(4,2,1) # 1.sırada 3x2 lik alt tablo
plt.title("orjinal resim")
plt.imshow(img)

plt.subplot(4,2,2) # 2.sırada 3x2 lik alt tablo
plt.title("img+img")
plt.imshow(img+img)

plt.subplot(4,2,3) # 3.sırada 3x2 lik alt tablo
plt.title("img-img")
plt.imshow(img-img)

plt.subplot(4,2,4) 
plt.title("np.flip")
plt.imshow(np.flip(img,0)) # 0 x eksenine göre yansıma alır

plt.subplot(4,2,5) 
plt.title("np.flip")
plt.imshow(np.flip(img,1))

plt.subplot(4,2,6) 
plt.title("np.flip")
plt.imshow(np.flip(img,2))

plt.subplot(4,2,7) 
plt.title("np.fliplr")
plt.imshow(np.fliplr(img)) # left to rigt

plt.subplot(4,2,8) 
plt.title("np.flipud")
plt.imshow(np.flipud(img)) # updown


plt.show()












