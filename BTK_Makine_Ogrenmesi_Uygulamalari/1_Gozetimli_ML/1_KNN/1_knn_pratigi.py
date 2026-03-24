import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
df =pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target

knn = KNeighborsClassifier(n_neighbors=3)
