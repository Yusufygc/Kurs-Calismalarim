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

#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
# GERI ELEME YONTEMINI KULLANIYORUZ en yuksek p degerine sahip olani eleyecegiz
# MODELIN VE DEGISKENLERIN BASARISI ILE ILGILI BIR SISTEM KURUYORUZ
import statsmodels.api as sm
import numpy as np


X = np.append(arr =np.ones((22,1)).astype(int), values=veri ,axis=1)# formuldeki betasifir degerini ekliyoruz

X_liste = veri.iloc[:,[0,1,2,3,4,5]].values # tum verileri bir listede tutuyoruz (bagimsiz degiskenleri)

X_liste =np.array(X_liste, dtype=float)

model =sm.OLS(boy, X_liste).fit() # boyla diger verilerin arasindaki baglantiyi kuruyoruz
#istatiksel degerlerimizi cikartiyor
print(model.summary())

#---------------------------------------------------------------------------------#

# X5 DEGERINI CIKARTIP TEKRAR DEGERLENDIRIYORUZ CUNKU EN YUKSEK P DEGERI ONUN

X_liste = veri.iloc[:,[0,1,2,3,5]].values # tum verileri bir listede tutuyoruz (bagimsiz degiskenleri)

X_liste =np.array(X_liste, dtype=float)

model =sm.OLS(boy, X_liste).fit() # boyla diger verilerin arasindaki baglantiyi kuruyoruz
#istatiksel degerlerimizi cikartiyor
print(model.summary())

"""
p VALUE DEGERINE GORE MODEL BASARIMLARINI DEGERLENDIRDIK 
GERI ELEME YONTEMI KULLANARAK HIC KATKISI OLMAYAN VERIYI MODEL EGITIMINDEN CIKARDIK

  OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.885
Model:                            OLS   Adj. R-squared:                  0.849
Method:                 Least Squares   F-statistic:                     24.69
Date:                Sat, 26 Jul 2025   Prob (F-statistic):           5.41e-07
Time:                        17:45:48   Log-Likelihood:                -73.950
No. Observations:                  22   AIC:                             159.9
Df Residuals:                      16   BIC:                             166.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1           114.0688      8.145     14.005      0.000      96.802     131.335
x2           108.3030      5.736     18.880      0.000      96.143     120.463
x3           104.4714      9.195     11.361      0.000      84.978     123.964
x4             0.9211      0.119      7.737      0.000       0.669       1.174
x5             0.0814      0.221      0.369      0.717      -0.386       0.549
x6           -10.5980      5.052     -2.098      0.052     -21.308       0.112
==============================================================================
Omnibus:                        1.031   Durbin-Watson:                   2.759
Prob(Omnibus):                  0.597   Jarque-Bera (JB):                0.624
Skew:                           0.407   Prob(JB):                        0.732
Kurtosis:                       2.863   Cond. No.                         524.
==============================================================================


USTTEKI SONUCLARDA X5 IN DEGERI 0.05 TEN BUYUK OLDUGU ICIN CIKARDIK VE TERKRAR
EGITTIK ISTERSEK X6 YI DA CIKARABILIRIZ CUNKU O DA DEFAULT DEGERE COK YAKIN


                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.884
Model:                            OLS   Adj. R-squared:                  0.857
Method:                 Least Squares   F-statistic:                     32.47
Date:                Sat, 26 Jul 2025   Prob (F-statistic):           9.32e-08
Time:                        17:45:48   Log-Likelihood:                -74.043
No. Observations:                  22   AIC:                             158.1
Df Residuals:                      17   BIC:                             163.5
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1           115.6583      6.734     17.175      0.000     101.451     129.866
x2           109.0786      5.200     20.978      0.000      98.108     120.049
x3           106.5445      7.090     15.026      0.000      91.585     121.504
x4             0.9405      0.104      9.029      0.000       0.721       1.160
x5           -11.1093      4.733     -2.347      0.031     -21.096      -1.123
==============================================================================
Omnibus:                        0.871   Durbin-Watson:                   2.719
Prob(Omnibus):                  0.647   Jarque-Bera (JB):                0.459
Skew:                           0.351   Prob(JB):                        0.795
Kurtosis:                       2.910   Cond. No.                         397.
==============================================================================

Notes:


1. Modelin Genel Uyum Gücü:
R-squared (R²) = 0.885: Bağımsız değişkenler (x1–x6), 
bağımlı değişken y'deki değişimin %88.5'ini açıklıyor. 
Bu oldukça yüksek bir uyum gücüne işaret eder.

Adj. R-squared = 0.849: Modeldeki değişken sayısına göre düzeltilmiş R². 
Bu da güçlü bir model olduğunu gösterir.

2. Modelin Anlamlılığı:
F-statistic = 24.69, 
Prob (F-statistic) = 5.41e-07: 
Modelin tamamı anlamlı; yani en az bir değişkenin 
y üzerindeki etkisi istatistiksel olarak anlamlı.

3. Değişkenlerin Anlamlılığı:
| Değişken | Katsayı (coef) | p-değeri (P>|t|) | Yorum |
|----------|----------------|------------------|-------|
| x1 | 114.07 | 0.000 | Çok anlamlı (y üzerinde pozitif etkili) |
| x2 | 108.30 | 0.000 | Çok anlamlı (y üzerinde pozitif etkili) |
| x3 | 104.47 | 0.000 | Çok anlamlı (y üzerinde pozitif etkili) |
| x4 | 0.921 | 0.000 | Anlamlı (y üzerinde pozitif etkili) |
| x5 | 0.081 | 0.717 | Anlamsız (y üzerindeki etkisi önemsiz) |
| x6 | -10.598 | 0.052 | Sınırda anlamlı (p ≈ 0.05); negatif etkili olabilir |

Not: Genellikle p < 0.05 anlamlı kabul edilir. x5 tamamen anlamsız, x6 sınırda kabul edilebilir.

4. Model Diagnostikleri:
Durbin-Watson = 2.759: Artıklar (hatalar) arasında otokorelasyon olup olmadığını test eder. 2’ye yakınsa otokorelasyon yoktur. Bu değer otokorelasyon olmadığını gösteriyor.

Omnibus = 1.031, Prob(Omnibus) = 0.597 ve Jarque-Bera = 0.624, Prob(JB) = 0.732: Hataların normal dağılıma uygunluğunu test eder. P > 0.05 olduğu için hatalar normal dağılmış.

5. Katsayıların Yorumu:
x1–x4’ün katsayıları pozitif ve anlamlı → Bu değişkenlerdeki artış, y’yi anlamlı düzeyde artırıyor.

x5’in etkisi anlamsız → Bu değişken modelden çıkarılabilir.

x6’nın katsayısı negatif, p ≈ 0.05 → Bu değişken dikkatle değerlendirilip, gerekirse tutma/çıkarma kararı verilebilir.

6. Modelin Geliştirilmesi:
x5 çıkarılarak model tekrar eğitilebilir; bu durumda AIC/BIC değerleri gözlenip model iyileşiyor mu kontrol edilebilir.

Çoklu doğrusal bağlantı (multicollinearity) riskine karşı VIF (Variance Inflation Factor) değerlendirilebilir (yüksekse dikkat!).

Sonuç:
Model genel olarak güçlü ve anlamlı. Ancak, x5 çıkarılarak daha sade ve belki daha iyi bir model elde edilebilir. x6 için ise veri ve bağlam değerlendirilerek karar verilmelidir.
"""







