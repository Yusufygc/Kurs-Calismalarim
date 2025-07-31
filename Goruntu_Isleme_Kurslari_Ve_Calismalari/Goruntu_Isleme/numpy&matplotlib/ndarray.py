import numpy as np

# ndarray ---> n dimensional array yani çok boyutlu diziler 

x = np.array([[-2,3,-6,2],[5,3,7,-1]],np.int16) # uint te negatif sayılar yoktur o yüzden int alacağız

print(x)
print(x.shape) # satır sütun mevzusunu söyler

print(x.ndim) # kaç boyut olduğunu söyler

print(x.dtype)

print(x.size) # eleman sayısı

print(x.T) # transpozesini alır