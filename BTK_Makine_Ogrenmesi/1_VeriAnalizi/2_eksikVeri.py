# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:19:13 2025

@author: ysfygc
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv("eksikveri.csv")

df = pd.DataFrame(data)

print(df)

imputer = SimpleImputer(missing_values=np.nan,strategy='mean') # nan olan degererin yerine o sutunun ortalama degerini yazcaz

Yas = df.iloc[:,1:4].values
print(Yas)# yas boy kilo verisi beraber geldi

imputer = imputer.fit(Yas[:,1:4]) # burda ortalama veriyi ogrendi imputer eksik verilerin yerine koyulacak degeri
Yas[:,1:4] = imputer.transform(Yas[:,1:4]) # yas taki nan degerler degisecek

print(Yas)




