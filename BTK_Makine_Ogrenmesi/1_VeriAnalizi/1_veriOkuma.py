import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("1_VeriAnalizi/veriler.csv")

df = pd.DataFrame(data)

print(df)

boy = df[['boy']]

boykilo = df[['boy','kilo']]

print(boykilo)


