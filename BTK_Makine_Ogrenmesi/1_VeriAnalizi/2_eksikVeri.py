# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:19:13 2025

@author: ysfygc
"""

import pandas as pd
from sklearn.impute import SimpleImputer


data = pd.read_csv("eksikveri.csv")

df = pd.DataFrame(data)

print(df)

