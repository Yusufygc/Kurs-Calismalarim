# -*- coding: utf-8 -*-
import pandas as pd 

veriler = pd.read_csv("D:/1KodCalismalari/Kurs-Calismalarim/BTK_Makine_Ogrenmesi/1_VeriAnalizi/veriler.csv")

x= veriler.iloc[:,1:4]
y = veriler.iloc[:,4:]

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
from sklearn.model_selection import train_test_split

x_train , x_test ,y_train ,y_test = train_test_split(x,y, test_size=0.33 ,random_state=0)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train = sc.fit_transform(x_train) # fit egitmedir
X_test = sc.transform(x_test) # transform kullanmadir yukarda egitilip ogrenilen burda kullanilir

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
from sklearn.linear_model import LogisticRegression

logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
y_predict = logr.predict(X_test)

print(y_predict)
print(y_test)



























