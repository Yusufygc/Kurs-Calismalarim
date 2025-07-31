import numpy as np

x = np.empty([4,4],np.uint8)

print("x : ",x)
print("----------")

y = np.full((3,3,3),dtype=np.int16,fill_value=5) # 3x3 lü 3 derinliğe sahip 5'lerden oluşan bir matris

print("y : ",y)
print("----------")


o = np.ones((2,5,5),dtype=np.int8) # 2 derinliğe sahip 5x5 lik matris

print("o : ",o)
print("----------")


z = np.zeros((2,5,5),dtype=np.int8) # 2 derinliğe sahip 5x5 lik matris

print("z : ",z)
print("----------")



