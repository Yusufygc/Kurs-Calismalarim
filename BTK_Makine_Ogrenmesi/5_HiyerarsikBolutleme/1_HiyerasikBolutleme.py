import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('D:/1KodCalismalari/Kurs-Calismalarim/BTK_Makine_Ogrenmesi/4_k-Means/musteriler.csv')


X = veriler.iloc[:,3:].values #<class 'numpy.ndarray'> yas ve hacim

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3 , init='k-means++')
kmeans.fit(X)

sonuclar =[]

for i in range(1,10):
    kmeans = KMeans(n_clusters=i, init='k-means++',random_state=123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)


#Hiyerarsik Bolutleme

from sklearn.cluster import AgglomerativeClustering

ac = AgglomerativeClustering(n_clusters=4,linkage='ward')

Y_tahmin = ac.fit_predict(X)
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1],s=100, c='red')
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1],s=100, c='blue')
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1],s=100, c='green')
plt.scatter(X[Y_tahmin==3,0],X[Y_tahmin==3,1],s=100, c='yellow')
plt.show()

import scipy.cluster.hierarchy as sch

dendogram =sch.dendrogram(sch.linkage(X,method='ward'))
plt.show()


