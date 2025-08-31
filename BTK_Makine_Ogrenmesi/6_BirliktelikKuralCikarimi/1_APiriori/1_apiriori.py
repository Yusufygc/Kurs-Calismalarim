
import pandas as pd

veriler = pd.read_csv('D:/1KodCalismalari/Kurs-Calismalarim/BTK_Makine_Ogrenmesi/6_BirliktelikKuralCikarimi/1_APiriori/sepet.csv',header=None)
#kolon basliklarimiz olmadigi icin header none yaptik

t=[]

for i in range(0,7051):
    t.append([str(veriler.values[i,j]) for j in range(0,20)])



from apyori import apriori

kurallar=apriori(t,min_support =0.01 , min_confidence = 0.2 , min_lift =3, min_length=2)


print(list(kurallar))

"""
Bu kod, alışveriş sepeti verilerinden birliktelik kuralları çıkarmak için 
yazılmıştır. Önce pandas ile sepet.csv dosyası okunur ve her satır (müşteri sepeti) 
20 üründen oluşan bir listeye dönüştürülür. Böylece t listesi içinde tüm müşterilerin alışverişleri tutulur. 
Daha sonra apyori kütüphanesinden Apriori algoritması çağrılır. 
Parametreler: min_support=0.01 (ürünlerin en az %1 birlikte görülmesi), 
min_confidence=0.2 (kuralın güvenilirliğinin en az %20 olması), 
min_lift=3 (ürünlerin birlikte alınma olasılığının bağımsızlığa göre 3 kat fazla olması) 
ve min_length=2 (kuralın en az 2 ürün içermesi). 
Son aşamada bulunan kurallar listeye çevrilerek ekrana yazdırılır. 
Çıktı, "Süt alanların ekmek alma ihtimali" gibi ürünler arasındaki ilişkileri gösterir.
"""






































