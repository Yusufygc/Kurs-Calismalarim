import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)

print(x)

y = x 

# plt.plot(x,y)

# plt.plot(x,y,"o")

# plt.plot(x,y,"o-")

plt.plot(x,y,"o--")
plt.plot(-x,y)
plt.plot(x,-y)
plt.title("Matplotlib deneme")
plt.show()
