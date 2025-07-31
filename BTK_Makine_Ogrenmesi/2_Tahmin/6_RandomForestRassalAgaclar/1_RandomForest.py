import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("D:/1KodCalismalari/Python-Calismalari/BTK_Makine_Ogrenmesi/2_Tahmin/3_PolinomRegresyon/maaslar.csv")


x = veriler.iloc[:,1:2] #dataframe
y = veriler.iloc[:,2:]

X=x.values # numpy array
Y=y.values


#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# DECISION TREE
from sklearn.ensemble import RandomForestRegressor

rf_reg = RandomForestRegressor(n_estimators=10 ,random_state=0)
# n_estimators=10 kac tane decision tree cizilecek onu belirtir
rf_reg.fit(X, Y.ravel())

print(rf_reg.predict([[6.6]]))

plt.scatter(X,Y,color ='red')
plt.plot(X,rf_reg.predict(x) , color ='green')
plt.show()
