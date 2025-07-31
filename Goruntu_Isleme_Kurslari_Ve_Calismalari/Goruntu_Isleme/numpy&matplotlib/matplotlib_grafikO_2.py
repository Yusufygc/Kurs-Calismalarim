import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)

plt.plot(x,[y**2 for y in x] )
 
plt.plot(x,[y**3 for y in x] )

plt.plot(x,2*x)
plt.plot(x,5.2*x)

plt.legend(["x**2","x**3","2x","5.2x"],loc='upper left') # grafikleri tek tek adlandırmayı sağlar. sol üst köşeyi verir upper center orta üst ....

plt.grid(True) # Izgara oluştur kareli sistem haline getiriyor

plt.xlabel("np.arrange den gelen değerler") # x eksenine iism verme
plt.ylabel("x e bağlı sonuçlar") # y eksenine isim verme

plt.axis([0,2 , 0,10]) # ilk iki argüman x in min max noktaları
plt.title("basit grafik")

# print(plt.axis()) # x ve y eksenlerindeki max ve min noktaları gösterir

plt.savefig("C:\\vscode\\Python\\Teknofest\\numpy&matplotlib\\plt.png")

plt.show()
