import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

data = pd.read_csv("veriler.csv")

df = pd.DataFrame(data)

Yas = df.iloc[:,1:4].values
#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# ULKELER ICIN ENCODING ISLEMI

ulke = df.iloc[:,0:1].values #İlk sütunu alır, NumPy 2D array'e çevirir
#print(ulke[:,0]) #	Tüm ülke değerlerini 1D NumPy array olarak verir

labelEnocoder = preprocessing.LabelEncoder()
ulke[:,0] = labelEnocoder.fit_transform(df.iloc[:,0])

oneHotEncoder = preprocessing.OneHotEncoder()
ulke = oneHotEncoder.fit_transform(ulke).toarray()

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# CINSIYET ICIN ENCODING ISLEMI

cinsiyet = df.iloc[:,-1:].values #İlk sütunu alır, NumPy 2D array'e çevirir
#print(ulke[:,0]) #	Tüm ülke değerlerini 1D NumPy array olarak verir

labelEnocoder = preprocessing.LabelEncoder()
cinsiyet[:,-1] = labelEnocoder.fit_transform(df.iloc[:,-1])

oneHotEncoder = preprocessing.OneHotEncoder()
cinsiyet = oneHotEncoder.fit_transform(cinsiyet).toarray()

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# VERILERIN BIRLESTIRILIP DATAFRAME OLUSTURULMASI
sonuc = pd.DataFrame(data=ulke, index=range(22), columns=['fr','tr','us'])

yenidf = pd.DataFrame(Yas, index=range(22), columns=['boy','kilo','yas'])

birlestirilmisDf = pd.concat([sonuc,yenidf], axis=1)


cinsiyetDf =pd.DataFrame(cinsiyet[:,:1], index=range(22), columns=['cinsiyet'])

birlestirilmisTamDf = pd.concat([birlestirilmisDf,cinsiyetDf], axis=1)


#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# VERILERIN TEST VE TRAIN OLARAK BOLUNMESI

from sklearn.model_selection  import train_test_split

x_train,x_test, y_train, y_test = train_test_split(birlestirilmisDf,cinsiyetDf,test_size=0.33,random_state=0)

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# REGRESYON MODELININ OLUSTURULMASI
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_predict =regressor.predict(x_test)


#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# BOY TAHMINI YAPMAK ICIN VERI MANUPILASYONU YAPIYORUZ

boy = birlestirilmisTamDf.iloc[:,3:4].values
print(boy)

sol = birlestirilmisTamDf.iloc[:,:3]
sag = birlestirilmisTamDf.iloc[:,4:]

veri =pd.concat([sol,sag],axis=1)
print(veri)
#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# Boy icin verileri tekrar bolduk \ yeni bir egitim ve tahmin islemi yapiyoruz

x_train,x_test, y_train, y_test = train_test_split(veri,boy,test_size=0.33,random_state=0)

regressor2 = LinearRegression()
regressor2.fit(x_train, y_train)

y_predict2 =regressor2.predict(x_test)











