import matplotlib.pyplot as plt
import numpy as np

"""
N =11
x = np.linspace(0,10,N) # 0-10 arası birbiriyle eşit aralıkta sayı oluşturma 
# print(x)
y = x

plt.plot(x,y,"o--")

plt.axis("off") # eksenlerdeki yazıları siler
"""

z = [ 1,3,5,7,9,11]

plt.plot(z,[a**2 for a in z])


plt.show()