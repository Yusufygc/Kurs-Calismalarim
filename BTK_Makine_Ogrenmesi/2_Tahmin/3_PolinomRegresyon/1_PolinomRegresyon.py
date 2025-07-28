import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("maaslar.csv")


x = veriler.iloc[:,1:2] #dataframe
y = veriler.iloc[:,2:]

X=x.values # numpy array
Y=y.values

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# Lineer Regresyonu Deniyoruz

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X,Y)

plt.scatter(X,Y)
plt.plot(x, lin_reg.predict(X))

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# Polinomal Regresyon
from sklearn.preprocessing import PolynomialFeatures
poly_reg =PolynomialFeatures(degree=2) # 2.dereceden olusan bir nesne olusturduk

x_poly = poly_reg.fit_transform(X) 
print(x_poly)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

plt.scatter(X,Y)
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X))) # lineer regresyon da kullanmak icin polinoml duzeyde denklestirdik verileri

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
poly_reg =PolynomialFeatures(degree=4) # 4.dereceden olusan bir nesne olusturduk

x_poly = poly_reg.fit_transform(X) 
print(x_poly)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

plt.scatter(X,Y)
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)))

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# TAHMINLER

print(lin_reg.predict([[11]]))
print(lin_reg.predict([[6.6]]))

print(lin_reg2.predict(poly_reg.fit_transform([[6.6]])))
print(lin_reg2.predict(poly_reg.fit_transform([[11]])))