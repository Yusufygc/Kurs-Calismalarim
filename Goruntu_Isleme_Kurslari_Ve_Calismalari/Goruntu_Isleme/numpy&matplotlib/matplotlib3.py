import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("C:\\vscode\\Python\\Teknofest\\numpy&matplotlib\\coins.jpg")

print(img)

print("type =",type(img))

print("shape =",img.shape)

print("ndim =",img.ndim)

print("size =",img.size)

print("dtype =",img.dtype)


print("red kanal : ",img[50,50,0]) #matplo ta RGB o yüzddn 0 girdik
print("green kanal : ",img[50,50,1])
print("blue kanal : ",img[50,50,2])

print("rgb kanal : ",img[50,50,:])





plt.imshow(img)
plt.show()








