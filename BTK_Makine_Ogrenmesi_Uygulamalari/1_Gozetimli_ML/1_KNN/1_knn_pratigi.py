import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

cancer = load_breast_cancer()
df =pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target

X = cancer.data
y = cancer.target

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.30, random_state=42)

# ölçeklendirme- normalizasyon
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test =scaler.transform(X_test)


# eğitim 
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)

# değerlendirme : test 
y_pred = knn.predict(X_test)
accuracy=accuracy_score(y_test, y_pred)

cf_matris = confusion_matrix(y_test, y_pred)
print(cf_matris)

# parametre ayarı

