import matplotlib.pyplot as plt
import numpy as np
import cv2

path = "C:\\vscode\\Python\\Teknofest\\numpy&matplotlib\\smile.jpg"
img = cv2.imread(path) # bgr okur
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img) # rgb gösterir


img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img,cmap="gray",interpolation="BICUBIC") # griye çevirmek için prosedürel işlemler 

plt.show()
















