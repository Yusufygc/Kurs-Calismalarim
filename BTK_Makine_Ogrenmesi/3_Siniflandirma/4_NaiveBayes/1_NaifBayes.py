
import pandas as pd 

veriler = pd.read_csv("D:/1KodCalismalari/Kurs-Calismalarim/BTK_Makine_Ogrenmesi/1_VeriAnalizi/veriler.csv")

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

y_predict = logr.predict(X_test)


#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# KARMASIKLIK MATRISI
from sklearn.metrics import confusion_matrix

cfMatrix = confusion_matrix(y_test,y_predict)


#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# KNN

from sklearn.neighbors import KNeighborsClassifier

knn =KNeighborsClassifier(n_neighbors=5 , metric='minkowski')
knn.fit(X_train, y_train)

knn_y_predict = knn.predict(X_test)

knn_cfMatrix = confusion_matrix(y_test,knn_y_predict)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# SVM
from sklearn.svm import SVC

svc = SVC(kernel='linear') # rbf, poly ,sigmoid vb denenebilir kernel trick burada uygulanir
svc.fit(X_train, y_train)

svc_y_pred =svc.predict(X_test)

svc_cfMatrix = confusion_matrix(y_test,svc_y_pred)

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# NAIVE BAYES

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
 
gnb.fit(X_train, y_train)

gnb_y_pred =gnb.predict(X_test)

gnb_cfMatrix = confusion_matrix(y_test,svc_y_pred)

print(gnb_cfMatrix)






















