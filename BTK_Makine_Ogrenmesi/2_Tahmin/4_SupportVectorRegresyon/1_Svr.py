import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("D:/1KodCalismalari/Python-Calismalari/BTK_Makine_Ogrenmesi/2_Tahmin/3_PolinomRegresyon/maaslar.csv")


x = veriler.iloc[:,1:2] #dataframe
y = veriler.iloc[:,2:]

X=x.values # numpy array
Y=y.values

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# OZNITELIK OLCEKLEME SVR de KRITIK bir konu

from sklearn.preprocessing import StandardScaler

sc1 =StandardScaler()
x_olcekli =sc1.fit_transform(X)
sc2=StandardScaler()
y_olcekli =sc2.fit_transform(Y)

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# SVR MODELI
from sklearn.svm import SVR

svr = SVR(kernel ='rbf')
svr.fit(x_olcekli,y_olcekli)

plt.scatter(x_olcekli,y_olcekli,color='red')
plt.plot(x_olcekli, svr.predict(x_olcekli))













