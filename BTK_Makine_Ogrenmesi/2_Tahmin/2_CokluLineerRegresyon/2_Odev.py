# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import preprocessing

# Veriyi oku
data = pd.read_csv("odev_tenis.csv")
df = pd.DataFrame(data)
#--------------------------------------------------------------#
#--------------------------------------------------------------#
# OUTLOOK sütunu için label ve one-hot encoding işlemleri

# outlook sütununu al (2D array)
outlook = df.iloc[:, 0:1].values

# Label encoding (kategorileri sayıya çevir)
labelEncoder = preprocessing.LabelEncoder()
outlook[:, 0] = labelEncoder.fit_transform(df.iloc[:, 0])

# One-hot encoding (her kategori için ayrı sütun)
oneHotEncoder = preprocessing.OneHotEncoder()
outlook = oneHotEncoder.fit_transform(outlook).toarray()

# One-hot encoding sonucu DataFrame oluştur
outlookDf = pd.DataFrame(outlook, columns=["sunny", "overcast", "rainy"])
print(outlookDf)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# WINDY sütunu için encoding işlemleri

# windy sütununu 2D DataFrame olarak al
windy = df[["windy"]]

# Label encoding (True/False → 1/0)
df["windy"] = labelEncoder.fit_transform(df["windy"])

# One-hot encoding uygulayalım
windy = oneHotEncoder.fit_transform(windy).toarray()

# İlk sütunu alarak DataFrame oluştur (örneğin windy=False)
windyDf = pd.DataFrame(windy[:, 0], columns=["windy"])
print(windyDf)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# TEMPERATURE ve HUMIDITY sütunlarını ayır

tempHum = df.iloc[:, 1:3].values
tempHumDf = pd.DataFrame(tempHum, columns=["temperature", "humidity"])
print(tempHumDf)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# OUTLOOK, TEMPERATURE, HUMIDITY verilerini birleştir

df1 = pd.concat([outlookDf, tempHumDf], axis=1)
print(df1)

# WINDY verisini de ekleyerek tüm veri setini oluştur
temizVeTamDf = pd.concat([df1, windyDf], axis=1)
print(temizVeTamDf)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# PLAY sütununu hedef değişken olarak ayrı tutalım

# orijinal play sütununu al (label encoding yapılmadan)
play = df.iloc[:, -1]

# Label encoding ile play sütununu sayısal hale getir
df["play"] = labelEncoder.fit_transform(df["play"])

# One-hot encoding uygulayalım (2D çıktı verir)
play = oneHotEncoder.fit_transform(df[["play"]]).toarray()
print(play)

# Sadece ilk sütunu alarak play DataFrame oluştur
playDf = pd.DataFrame(play[:, [0]], columns=["play"])
print(playDf)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# VERİLERİ eğitim (train) ve test olarak ayırıyoruz

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    temizVeTamDf, playDf, test_size=0.33, random_state=0)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# LINEAR REGRESSION MODELİ oluşturuluyor

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Test verisi ile tahmin yap
y_predict = regressor.predict(x_test)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# GERI ELEME (BACKWARD ELIMINATION) yöntemi ile model sadeleştirme

import statsmodels.api as sm
import numpy as np

# Sadece analiz için tüm bağımsız değişkenler (6 sütun) + sabit beta_0
X_liste = temizVeTamDf.iloc[:, [0, 1, 2, 3, 4, 5]].values.astype(float)
X_with_const = sm.add_constant(X_liste)

# Bağımlı değişken: play sütunu (1D array, LabelEncoder uygulanmış hali)
# Bu kısımda direkt df["play"] kullan çünkü label encoder uygulanmıştı
y = df["play"].values

# İlk OLS modelini oluştur
model = sm.OLS(y, X_with_const).fit()
print("\nİlk OLS Sonuçları:")
print(model.summary())

# Geri Eleme işlemi başlat
X_opt = X_with_const.copy()
columns = ["const", "sunny", "overcast", "rainy", "temperature", "humidity", "windy"]

while True:
    p_values = pd.Series(model.pvalues, index=columns)  # HATA BURADA DÜZELTİLDİ
    max_p = p_values.max()
    
    if max_p > 0.05:
        excluded_var = p_values.idxmax()
        excluded_pos = columns.index(excluded_var)
        
        print(f"\nÇıkarılıyor: {excluded_var} (p={max_p:.4f})")
        
        # Kolonu çıkar ve veriyi güncelle
        X_opt = np.delete(X_opt, excluded_pos, axis=1)
        columns.pop(excluded_pos)
        
        # Yeni model
        model = sm.OLS(y, X_opt).fit()
        print(model.summary())
    else:
        print("\nTüm kalan değişkenler anlamlı. Geri eleme tamamlandı.")
        print(f"Kalan değişkenler: {columns}")
        break
#--------------------------------------------------------------#
#--------------------------------------------------------------#
# OLS SONUÇLARINI DOSYAYA KAYDET (dökümantasyon)

import os

dosya_adi = "ols_raporu.txt"

# Eğer varsa eski dosyayı sil (yeni rapor için)
if os.path.exists(dosya_adi):
    os.remove(dosya_adi)

# İlk modeli yazdır
def yaz_rapor(model, columns, step):
    ols_text = model.summary().as_text()
    notes_start = ols_text.find("Notes:")
    if notes_start != -1:
        ols_text = ols_text[:notes_start].rstrip()
    
    with open(dosya_adi, "a", encoding="utf-8") as file:  # 'a' ile append modu
        file.write(f"\n{'='*60}\n")
        file.write(f"Adım {step} - Model Özeti\n")
        file.write(f"{'-'*60}\n")
        file.write(ols_text)
        file.write("\n\nKalan değişkenler:\n")
        file.write(", ".join(columns))
        file.write("\n\n")

# İlk modeli ve adımı başlat
X_opt = X_with_const.copy()
columns = ["const", "sunny", "overcast", "rainy", "temperature", "humidity", "windy"]

model = sm.OLS(y, X_opt).fit()
step = 1
yaz_rapor(model, columns, step)
print(model.summary())

# Geri eleme döngüsü
while True:
    p_values = pd.Series(model.pvalues, index=columns)
    max_p = p_values.max()

    if max_p > 0.05:
        excluded_var = p_values.idxmax()
        excluded_pos = columns.index(excluded_var)
        print(f"\nÇıkarılıyor: {excluded_var} (p={max_p:.4f})")

        X_opt = np.delete(X_opt, excluded_pos, axis=1)
        columns.pop(excluded_pos)

        model = sm.OLS(y, X_opt).fit()
        step += 1
        yaz_rapor(model, columns, step)
        print(model.summary())
    else:
        print("\nTüm kalan değişkenler anlamlı. Geri eleme tamamlandı.")
        print(f"Kalan değişkenler: {columns}")
        break

#--------------------------------------------------------------#
#--------------------------------------------------------------#
# Modelin Performansını Cross-Validation ile Değerlendirme

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Son modelde kalan bağımsız değişkenleri tekrar kullan
final_X = X_opt  # zaten optimal hale gelmişti
final_y = y

# Regressor modelini tanımla
regressor = LinearRegression()

# 5-Fold Cross-Validation ile R² (determinasyon katsayısı) hesapla
scores = cross_val_score(regressor, final_X, final_y, cv=5, scoring='r2')
print("Cross-Validation R² Skorları:", scores)
print("Ortalama R² Skoru:", scores.mean())
#--------------------------------------------------------------#
#--------------------------------------------------------------#

#Gerçek vs. Tahmin Grafik Çizimi

import matplotlib.pyplot as plt

# Modeli son haliyle tekrar eğit
regressor.fit(final_X, final_y)

# Tahmin yap
y_pred = regressor.predict(final_X)

# Grafik
plt.figure(figsize=(10, 6))
plt.plot(final_y, label="Gerçek Değerler", marker='o')
plt.plot(y_pred, label="Tahmin Edilen Değerler", marker='x')
plt.title("Gerçek vs. Tahmin Edilen PLAY Değerleri")
plt.xlabel("Veri Nokası")
plt.ylabel("PLAY")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


"""X_liste = sm.add_constant(X_liste)  # İlk sütun: sabit (1) numpy ile ekledigimiz kisim

# Bağımlı değişken: Etiketlenmiş play sütunu (1D array)
play = df["play"].values

# OLS regresyon modeli ile istatistiksel analiz yap
model = sm.OLS(play, X_liste).fit()

# Model özetini yazdır (p-değerlerine bakarak geri eleme yapılabilir)
print(model.summary())
"""
"""
 OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.483
Model:                            OLS   Adj. R-squared:                  0.160
Method:                 Least Squares   F-statistic:                     1.493
Date:                Sat, 26 Jul 2025   Prob (F-statistic):              0.292
Time:                        19:48:23   Log-Likelihood:                -4.9501
No. Observations:                  14   AIC:                             21.90
Df Residuals:                       8   BIC:                             25.73
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.9838      1.291      1.536      0.163      -0.994       4.962
x1             1.0062      0.493      2.039      0.076      -0.132       2.144
x2             0.5528      0.403      1.373      0.207      -0.376       1.482
x3             0.4248      0.510      0.833      0.429      -0.752       1.601
x4            -0.0143      0.025     -0.569      0.585      -0.072       0.044
x5            -0.0142      0.014     -1.031      0.333      -0.046       0.018
x6             0.4108      0.268      1.533      0.164      -0.207       1.029
==============================================================================
Omnibus:                        0.118   Durbin-Watson:                   1.317
Prob(Omnibus):                  0.943   Jarque-Bera (JB):                0.340
Skew:                           0.035   Prob(JB):                        0.844
Kurtosis:                       2.240   Cond. No.                     3.04e+18
==============================================================================


| Metrik                           | Sonuç                 | Yorum                                                           |
| -------------------------------- | --------------------- | --------------------------------------------------------------- |
| **R-squared**                    | 0.483                 | Model verinin %48’ini açıklıyor → zayıf/orta seviye             |
| **Adj. R-squared**               | 0.160                 | Düzeltme sonrası %16 → açıklama gücü düşük                      |
| **Prob (F-statistic)**           | 0.292 (> 0.05)        | Model **istatistiksel olarak anlamlı değil**                    |
| **p-value (x1)**                 | 0.076                 | Sınırda anlamlılık (x1 dikkat çekiyor)                          |
| **p-value (diğerleri)**          | > 0.1–0.5             | Anlamsız, modele katkısı az                                     |
| **Cond. No. (Kondisyon sayısı)** | 3.04e+18 → Çok yüksek | **Multicollinearity (değişkenler arası yüksek ilişki)** uyarısı |



"""





"""

windy ve play sutunlari label encoder ile cevrilebilirdi 
one hot encod ile ugrasmamiza gerek kalmazdi cunku 2 durum var


data = pd.read_csv("odev_tenis.csv")
df = pd.DataFrame(data)

data1 = data.apply(preprocessing.LabelEncoder().fit_transform) ile tum veriler 
label encode edilir ihtiyacimiz olani burdan cekebiliriz.

❗Ne Zaman OneHotEncoder Kullanmalısın?
Durum	                                    Kullanılacak Yöntem
Sadece 2 kategori varsa (binary)	        LabelEncoder yeterli
3+ kategori varsa (ör. outlook)	            OneHotEncoder önerilir
Lineer regresyonda anlamlılık önemliyse	    One-hot tercih edilebilir

Örnek: outlook = {sunny, overcast, rainy} → burada OneHotEncoder doğru seçim, çünkü 3 kategori var ve bunların sayısal sıralaması yok.


"""

"""

Aşağıda sadeleştirilmiş ve verimli hale getirilmiş kod yapısını paylaşıyorum. Bu versiyonda:

Tüm veriler hızlıca LabelEncoder ile sayısal hale getirilir.

Gerekli olan X (özellikler) ve y (hedef) düzgün şekilde ayrılır.

Lineer regresyon uygulanır.

Geri Eleme (OLS p-değer analizi) yapılır



import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Veriyi oku
df = pd.read_csv("odev_tenis.csv")

# Tüm veriyi LabelEncoder ile encode et (otomatik tüm sütunlar)
df_encoded = df.apply(preprocessing.LabelEncoder().fit_transform)
print("LabelEncoder sonrası veri:")
print(df_encoded)

# Özellikler (bağımsız değişkenler) ve hedef (bağımlı değişken) ayrımı
X = df_encoded.drop("play", axis=1)  # outlook, temperature, humidity, windy
y = df_encoded["play"]               # play (0 veya 1)

# Veriyi eğitim ve test olarak böl
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Lineer regresyon modeli kur ve eğit
model = LinearRegression()
model.fit(x_train, y_train)

# Test verisi ile tahmin yap
y_pred = model.predict(x_test)
print("\nTahmin edilen değerler:")
print(y_pred)

# -------------------------------
# Geri Eleme (Backward Elimination) ile önemli değişkenleri seçme

# Sabit ekle
X = sm.add_constant(X.values)

# İlk model
model = sm.OLS(y, X).fit()
print(model.summary())

# Geri Eleme Döngüsü
while True:
    p_values = model.pvalues
    max_p = p_values.max()
    if max_p > 0.05:
        excluded_idx = p_values.idxmax()
        print(f"\nÇıkarılıyor: {excluded_idx} (p={max_p:.4f})")
        X = np.delete(X, excluded_idx, axis=1)
        model = sm.OLS(y, X).fit()
        print(model.summary())
    else:
        break



| Kod Parçası                              | Açıklama                                     |
| ---------------------------------------- | -------------------------------------------- |
| `df.apply(LabelEncoder().fit_transform)` | Tüm sütunları otomatik olarak sayıya çevirir |
| `X = df_encoded.drop("play", axis=1)`    | Tahmin için kullanılacak veriler (features)  |
| `y = df_encoded["play"]`                 | Tahmin edilecek değişken                     |
| `LinearRegression`                       | Tahmin modelini kurar                        |
| `sm.OLS(y, X_with_const).fit()`          | Geri eleme için p-değerlerini analiz eder    |


"""



























