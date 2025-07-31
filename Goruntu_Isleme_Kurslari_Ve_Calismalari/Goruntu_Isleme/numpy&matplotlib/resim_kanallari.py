import matplotlib.pyplot as plt
import numpy as np

path = "C:\\vscode\\Python\\Teknofest\\numpy&matplotlib\\map.jpeg"
img = plt.imread(path)

red =img[:,:,0]
green =img[:,:,1]
blue =img[:,:,2]

output = [img,red,green,blue]
titles = ["orjinal resim","red","green","blue"]

for i in range(4):# yukardkiler 4 değer olduğu için
    plt.subplot(2,2,i+1)# alt grafikler oluşturur. i+1 olayı 0.grafik diye bir şey olmadığı için
    plt.axis("off")
    plt.title(titles[i])
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap="gray") # daha iyi anlamak için griye çevirdik
    plt.show()