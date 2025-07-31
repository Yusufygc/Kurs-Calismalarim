import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

veriler = pd.read_csv("D:/1KodCalismalari/Kurs-Calismalarim/BTK_Makine_Ogrenmesi/2_Tahmin/3_PolinomRegresyon/maaslar.csv")


x = veriler.iloc[:,1:2] #dataframe
y = veriler.iloc[:,2:]

X=x.values # numpy array
Y=y.values

#---------------------------------------------------#
# REGRESYON MODELINI OLUSTURMA ISLEMI               #
#---------------------------------------------------#

from sklearn.linear_model import LinearRegression # CTRL+I ile bilgi alabiliriz fonka tiklayip

lr = LinearRegression() 
lr.fit(X, Y)

print(' Linear Regresyon R2 degeri :' ,r2_score(Y, lr.predict((X))) )

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# Polinomal Regresyon
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg =PolynomialFeatures(degree=2) # 2.dereceden olusan bir nesne olusturduk
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

print('Polinomal Regresyon R2 degeri :',r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))


#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# SVR MODELI

from sklearn.preprocessing import StandardScaler
sc1 =StandardScaler()
x_olcekli =sc1.fit_transform(X)
sc2=StandardScaler()
y_olcekli =sc2.fit_transform(Y)

from sklearn.svm import SVR

svr = SVR(kernel ='rbf') # bu metrigi degistirek R2 degerini degistirebiliriz
svr.fit(x_olcekli,y_olcekli)

plt.scatter(x_olcekli,y_olcekli,color='red')
plt.plot(x_olcekli, svr.predict(x_olcekli))

print('SVR R2 degeri :',r2_score(y_olcekli, svr.predict(x_olcekli)))

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# DECISION TREE
from sklearn.tree import DecisionTreeRegressor

r_dt = DecisionTreeRegressor(random_state=0)

r_dt.fit(X, Y)

plt.scatter(X,Y,color ='red')
plt.plot(X,r_dt.predict(x) , color ='green')

print('Decision Tree R2 degeri :',r2_score(Y, r_dt.predict(X)))

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# Random Forest
from sklearn.ensemble import RandomForestRegressor

rf_reg = RandomForestRegressor(n_estimators=10 ,random_state=0)
# n_estimators=10 kac tane decision tree cizilecek onu belirtir
rf_reg.fit(X, Y.ravel())

print(rf_reg.predict([[6.6]]))

plt.scatter(X,Y,color ='red')
plt.plot(X,rf_reg.predict(X) , color ='green')
plt.show()
print('Random Forest R2 degeri       :',r2_score(Y, rf_reg.predict(X)))

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# R2 degerleri
print('Random Forest R2 degeri       :',r2_score(Y, rf_reg.predict(X)))
print('Decision Tree R2 degeri       :',r2_score(Y, r_dt.predict(X)))
print('SVR R2 degeri                 :',r2_score(y_olcekli, svr.predict(x_olcekli)))
print('Polinomal Regresyon R2 degeri :',r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))
print('Linear Regresyon R2 degeri    :',r2_score(Y, lr.predict((X))) )