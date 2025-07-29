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
from sklearn.tree import DecisionTreeRegressor

r_dt = DecisionTreeRegressor(random_state=0)

r_dt.fit(X, Y)

plt.scatter(X,Y,color ='red')
plt.plot(X,r_dt.predict(x) , color ='green')

# seviyeye gore maas tahmin
print(r_dt.predict([[11]]))
print(r_dt.predict([[6.6]]))
print(r_dt.predict([[1]]))
print(r_dt.predict([[2.4]]))
print(r_dt.predict([[1.6]]))
print(r_dt.predict([[1.5]]))
print(r_dt.predict([[1.1]]))
print(r_dt.predict([[1.9]]))
print(r_dt.predict([[2.05]]))