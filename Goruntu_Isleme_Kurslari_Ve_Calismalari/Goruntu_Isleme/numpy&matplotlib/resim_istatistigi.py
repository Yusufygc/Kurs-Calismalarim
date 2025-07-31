import matplotlib.pyplot as plt
import numpy as np

# resim = her bir pikselde renklerin belli bir oranda bir araya gelmesi ile oluşur

path = "C:\\vscode\\Python\\Teknofest\\numpy&matplotlib\\smile.jpg"
img = plt.imread(path) # bgr okur

print("min değer = " ,img.min()) # en küüçk piksel değeri
print("max değer = " ,img.max())
print("ortalama değer = " ,img.mean ()) # tüm renk değerlerinin ortalaması
print("medyan = " ,np.median(img))
print("average = " ,np.average(img))
print("mean1 = " ,np.mean(img))
"""
plt.imshow(img)
plt.show()
"""
