# -*- coding: utf-8 -*-

import pandas as pd 

veri = pd.read_csv("satislar.csv")

aylar =veri.iloc[:,0].values
# aylar =veri[["Aylar]]
aylarDf=pd.DataFrame(aylar,columns=["Aylar"])
#print(aylarDf)

satislar = veri.iloc[:,-1].values
# satislar = veri[["Satislar"]]
satislarDf = pd.DataFrame(satislar,columns=["Satislar"])
#print(satislarDf)

#---------------------------------------------------#
# VERILERIN TEST\TRAIN OLARAK AYRILMASI             #
#---------------------------------------------------#
from sklearn.model_selection import train_test_split

x_train, x_test , y_train , y_test = train_test_split(aylarDf,satislarDf ,test_size=0.33 ,random_state=0)

#---------------------------------------------------#
# VERILERIN OLCEKLENMESI              
# olceklemenin amaci verileri ayni duzeye getirmektir
#---------------------------------------------------#
from sklearn.preprocessing import StandardScaler

sc= StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#---------------------------------------------------#
# REGRESYON MODELINI OLUSTURMA ISLEMI               #
#---------------------------------------------------#

from sklearn.linear_model import LinearRegression # CTRL+I ile bilgi alabiliriz fonka tiklayip

lr = LinearRegression() 
"""
lr.fit(X_train,Y_train)# x trainden y traini tahmin edecek

tahmin = lr.predict(X_test) # olceklenmis veri uzerinden tahmin yaptik ama veriyi anlamak biraz zor           
"""
lr.fit(x_train,y_train)# x trainden y traini tahmin edecek
olceklenmemisTahmin =lr.predict(x_test)








