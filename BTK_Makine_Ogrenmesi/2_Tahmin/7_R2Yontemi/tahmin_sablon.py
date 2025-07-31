
#1.kutuphaneler
import pandas as pd
from sklearn.metrics import r2_score
# veri yukleme
veriler = pd.read_csv("D:/1KodCalismalari/Kurs-Calismalarim/BTK_Makine_Ogrenmesi/2_Tahmin/7_R2Yontemi/maaslar_yeni.csv")

#pandas df
x = veriler.iloc[:,2:5] #unvandan sonrasi
y = veriler.iloc[:,-1] #maas
# numpy array
X = x.values
Y = y.values

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#


# REGRESYON MODELININ OLUSTURULMASI
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X, Y)

y_predict =regressor.predict(X)

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# GERI ELEME YONTEMINI KULLANIYORUZ en yuksek p degerine sahip olani eleyecegiz
# MODELIN VE DEGISKENLERIN BASARISI ILE ILGILI BIR SISTEM KURUYORUZ
import statsmodels.api as sm
model =sm.OLS(Y, X).fit()
print(model.summary())
# X_liste = islenmisVeriDf.iloc[:,[0,1,2,3].values --> 3 numarali veri 0.545 p value oldugu icin cikti
# R2 sokuru dustu ama o yuzden veriri cikarmadan devam ediyoruz

#--------------------------------------------------------------#
#--------------------------------------------------------------#
#polynomial regression

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)

x_poly = poly_reg.fit_transform(X)
print(x_poly)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,Y)

print('Polynomial R2 degeri')
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))

#--------------------------------------------------------------#
#--------------------------------------------------------------#
#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler
import numpy as np

sc1=StandardScaler()
x_olcekli = sc1.fit_transform(X)

sc2=StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(Y.reshape(-1, 1)))

#--------------------------------------------------------------#

from sklearn.svm import SVR

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_olcekli,y_olcekli)

print('SVR R2 degeri')
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)))

#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Decision Tree Regresyon
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)

print('Decision Tree R2 degeri')
print(r2_score(Y, r_dt.predict(X)))
#--------------------------------------------------------------#
#--------------------------------------------------------------#

#Random Forest Regresyonu
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(X,Y)

print('Random Forest R2 degeri')
print(r2_score(Y, rf_reg.predict(X)))



# R2 degerleri
print('MLR R2 degeri                 :',r2_score(Y, regressor.predict(X)))
print('Random Forest R2 degeri       :',r2_score(Y, rf_reg.predict(X)))
print('Decision Tree R2 degeri       :',r2_score(Y, r_dt.predict(X)))
print('SVR R2 degeri                 :',r2_score(y_olcekli, svr_reg.predict(x_olcekli)))
print('Polinomal Regresyon R2 degeri :',r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))

"""
# Tahmin ceo
print("CEO Maas Tahmin")
print('Polinomal Regresyon :' ,lin_reg2.predict([[1,10,100]]))
print('SVR                 :' ,svr_reg.predict([[1,10,100]]))
#tahmin mudur
print("Mudur Maas Tahmin")
print('Polinomal Regresyon :' ,lin_reg2.predict([[4,10,100]]))
"""









