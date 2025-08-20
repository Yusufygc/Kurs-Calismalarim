import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('D:/1KodCalismalari/Kurs-Calismalarim/BTK_Makine_Ogrenmesi/4_k-Means/musteriler.csv')


X = veriler.iloc[:,3:].values #<class 'numpy.ndarray'> yas ve hacim

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3 , init='k-means++')
kmeans.fit(X)

print(kmeans.cluster_centers_)

"""
[[ 22069.41176471   5320.88235294]
 [104386.95652174   7289.13043478]
 [ 58643.47826087   5844.92753623]]
3 cludterin hacim ve maas orta noktalari

"""

sonuclar =[]

for i in range(1,10):
    kmeans = KMeans(n_clusters=i, init='k-means++',random_state=123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)


















