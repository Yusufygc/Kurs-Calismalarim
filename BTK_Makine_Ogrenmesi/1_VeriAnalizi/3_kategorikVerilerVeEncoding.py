
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

data = pd.read_csv("eksikveri.csv")

df = pd.DataFrame(data)

# EKSIK VERILERIN TAMAMLANMASI VE ENCODING ISLEMI
imputer = SimpleImputer(missing_values=np.nan,strategy='mean') # nan olan degererin yerine o sutunun ortalama degerini yazcaz
Yas = df.iloc[:,1:4].values# yas boy kilo verisi beraber geldi

imputer = imputer.fit(Yas[:,1:4]) # burda ortalama veriyi ogrendi imputer eksik verilerin yerine koyulacak degeri
Yas[:,1:4] = imputer.transform(Yas[:,1:4]) # yas taki nan degerler degisecek

ulke = df.iloc[:,0:1].values #İlk sütunu alır, NumPy 2D array'e çevirir
#print(ulke[:,0]) #	Tüm ülke değerlerini 1D NumPy array olarak verir

labelEnocoder = preprocessing.LabelEncoder()
ulke[:,0] = labelEnocoder.fit_transform(df.iloc[:,0])


oneHotEncoder = preprocessing.OneHotEncoder()
ulke = oneHotEncoder.fit_transform(ulke).toarray()
#label Encoderin cevirdigi sayilardan ogrenip bunu one hot encode etcek ve numpy array e cevirecek

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# VERILERIN BIRLESTIRILIP DATAFRAME OLUSTURULMASI
sonuc = pd.DataFrame(data=ulke, index=range(22), columns=['fr','tr','us'])

yenidf = pd.DataFrame(Yas, index=range(22), columns=['boy','kilo','yas'])

birlestirilmisDf = pd.concat([sonuc,yenidf], axis=1)

cinsiyet =df.iloc[:,-1].values

cinsiyetDf =pd.DataFrame(cinsiyet, index=range(22), columns=['cinsiyet'])

birlestirilmisTamDf = pd.concat([birlestirilmisDf,cinsiyetDf], axis=1)
print(birlestirilmisTamDf)

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

# VERILERIN TEST VE TRAIN OLARAK BOLUNMESI

from sklearn.model_selection  import train_test_split

x_train,x_test, y_train, y_test = train_test_split(birlestirilmisDf,cinsiyetDf,test_size=0.33,random_state=0)


















