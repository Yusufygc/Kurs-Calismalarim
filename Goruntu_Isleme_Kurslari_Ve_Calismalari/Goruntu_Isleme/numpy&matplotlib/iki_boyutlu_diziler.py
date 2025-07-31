import numpy as np

x = np.array([[1,2,3],[4,5,6]],np.int16)# tekrardan köşeli paranteze aldık
 
print("**************")
print(x)
print("**************")

print("\n")
print(x[0])
print("**************")
print(x[0][2])
print("**************") # ikiside aynı işlevi sağlar
print(x[0,2])

print(x[:,0])
print("**************") # hepsini tarayacak ve sıfırıncı indislerdekini yazdırır. her iki dizeninde
print(x[:,1])
print("**************")
print(x[:,2])
print("**************")
print(x[0,:]);print(x[1,:])
print("**************")










