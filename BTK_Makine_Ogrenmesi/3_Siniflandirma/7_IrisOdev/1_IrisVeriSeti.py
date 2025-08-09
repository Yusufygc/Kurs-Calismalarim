import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics

#---------------------------------------------------------------------#
# 1. Veri yükleme
veriler = pd.read_excel('Iris.xls')
x = veriler.iloc[:, 1:4]
y = veriler.iloc[:, 4:]

#---------------------------------------------------------------------#
# 2. Eğitim/Test Ayrımı
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=0
)

#---------------------------------------------------------------------#
# 3. Standardizasyon
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

#---------------------------------------------------------------------#
# Yardımcı fonksiyon
def print_results(name, cf_matrix):
    correct = np.trace(cf_matrix)
    total = np.sum(cf_matrix)
    wrong = total - correct
    print('#---------------------------------------------------------------------#')
    print(f"{name} :")
    print('#---------------------------------------------------------------------#')
    print(cf_matrix)
    print(f"✅ Doğru Tahmin Sayısı : {correct}")
    print(f"❌ Yanlış Tahmin Sayısı : {wrong}\n")

#---------------------------------------------------------------------#
# Logistic Regression
logr = LogisticRegression(random_state=0)
logr.fit(X_train, y_train)
lg_y_predict = logr.predict(X_test)
lg_cfMatrix = confusion_matrix(y_test, lg_y_predict)
print_results("Logistic Regression", lg_cfMatrix)

#---------------------------------------------------------------------#
# KNN
knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
knn.fit(X_train, y_train)
knn_y_predict = knn.predict(X_test)
knn_cfMatrix = confusion_matrix(y_test, knn_y_predict)
print_results("KNN", knn_cfMatrix)

#---------------------------------------------------------------------#
# SVM
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)
svc_y_pred = svc.predict(X_test)
svc_cfMatrix = confusion_matrix(y_test, svc_y_pred)
print_results("SVM", svc_cfMatrix)

#---------------------------------------------------------------------#
# Naive Bayes (hata düzeltilmiş)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
gnb_y_pred = gnb.predict(X_test)
gnb_cfMatrix = confusion_matrix(y_test, gnb_y_pred)
print_results("Naive Bayes", gnb_cfMatrix)

#---------------------------------------------------------------------#
# Karar Ağaçları
dtc = DecisionTreeClassifier(criterion='entropy')
dtc.fit(X_train, y_train)
dtc_y_pred = dtc.predict(X_test)
dtc_cfMatrix = confusion_matrix(y_test, dtc_y_pred)
print_results("Karar Ağaçları", dtc_cfMatrix)

#---------------------------------------------------------------------#
# Random Forest
rfc = RandomForestClassifier(n_estimators=10, criterion='entropy')
rfc.fit(X_train, y_train)
rfc_y_pred = rfc.predict(X_test)
rfc_cfMatrix = confusion_matrix(y_test, rfc_y_pred)
print_results("Random Forest", rfc_cfMatrix)

#---------------------------------------------------------------------#
# ROC, TPR, FPR değerleri (Iris-setosa için)
y_proba = rfc.predict_proba(X_test)
fpr, tpr, thold = metrics.roc_curve(y_test, y_proba[:, 0], pos_label='Iris-setosa')
print("FPR :", fpr)
print("TPR :", tpr)

"""
import pandas as pd 

veriler =pd.read_excel('Iris.xls')

x= veriler.iloc[:,1:4]
y = veriler.iloc[:,4:]

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
from sklearn.model_selection import train_test_split

x_train , x_test ,y_train ,y_test = train_test_split(x,y, test_size=0.33 ,random_state=0)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train = sc.fit_transform(x_train) # fit egitmedir
X_test = sc.transform(x_test) # transform kullanmadir yukarda egitilip ogrenilen burda kullanilir

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
from sklearn.linear_model import LogisticRegression

logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

lg_y_predict = logr.predict(X_test)


#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# KARMASIKLIK MATRISI
from sklearn.metrics import confusion_matrix

lg_cfMatrix = confusion_matrix(y_test,lg_y_predict)
print('#---------------------------------------------------------------------#')
print(" LogisticRegression :")
print('#---------------------------------------------------------------------#')
print(lg_cfMatrix)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# KNN

from sklearn.neighbors import KNeighborsClassifier

knn =KNeighborsClassifier(n_neighbors=5 , metric='minkowski')
knn.fit(X_train, y_train)

knn_y_predict = knn.predict(X_test)

knn_cfMatrix = confusion_matrix(y_test,knn_y_predict)
print('#---------------------------------------------------------------------#')
print(" KNN :")
print('#---------------------------------------------------------------------#')
print(knn_cfMatrix)
#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# SVM
from sklearn.svm import SVC

svc = SVC(kernel='linear') # rbf, poly ,sigmoid vb denenebilir kernel trick burada uygulanir
svc.fit(X_train, y_train)

svc_y_pred =svc.predict(X_test)

svc_cfMatrix = confusion_matrix(y_test,svc_y_pred)
print('#---------------------------------------------------------------------#')
print(" SVM :")
print('#---------------------------------------------------------------------#')
print(svc_cfMatrix)
#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# NAIVE BAYES

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
 
gnb.fit(X_train, y_train)

gnb_y_pred =gnb.predict(X_test)

gnb_cfMatrix = confusion_matrix(y_test,svc_y_pred)

print('#---------------------------------------------------------------------#')
print(" NAIVE BAYES :")
print('#---------------------------------------------------------------------#')
print(gnb_cfMatrix)
#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# KARAR AGACLARI

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion='entropy') # deafult paramtre ginidir
dtc.fit(X_train,y_train)

dtc_y_pred = dtc.predict(X_test)

dtc_cfMatrix = confusion_matrix(y_test,dtc_y_pred)
print('#---------------------------------------------------------------------#')
print("KARAR AGACLARI :")
print('#---------------------------------------------------------------------#')
print(dtc_cfMatrix)
#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# RANDOM FOREST

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators= 10 ,criterion='entropy')

rfc.fit(X_train,y_train)

rfc_y_pred = rfc.predict(X_test)

rfc_cfMatrix = confusion_matrix(y_test,rfc_y_pred)
print('#---------------------------------------------------------------------#')
print("RANDOM FOREST :")
print('#---------------------------------------------------------------------#')
print(rfc_cfMatrix)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
# 7. ROC , TPR, FPR değerleri 

from sklearn import metrics
y_proba = rfc.predict_proba(X_test)

fpr , tpr , thold = metrics.roc_curve(y_test,y_proba[:,0],pos_label='Iris-setosa')
print("FPR :",fpr)
print("TPR :",tpr)
"""



