**1. Apriori Algoritması**



**Nasıl çalışır?**



Tüm aday itemsetleri (ürün kombinasyonları) üretir.



Sonra bu itemsetlerin destek (support) değerlerini hesaplar.



Apriori özelliğini kullanır: “Bir itemset sık (frequent) değilse, onun üst kümeleri de sık olamaz.”



**Arama yaklaşımı:**



Yatay tarama (breadth-first search) yapar.



Yani veri tabanını defalarca tarayarak aday kümelerin desteklerini hesaplar.



**Avantajı:**



Basit ve anlaşılırdır.



**Dezavantajı:**



Büyük veri kümelerinde çok sayıda tarama yaptığı için yavaş çalışabilir.



**🔹 2. Eclat Algoritması**



**Nasıl çalışır?**



Veriyi dikey formatta (vertical data format) tutar:



Her ürün → onu satın alan müşteri ID’lerinin listesi.



İki ürünün birlikte alınma desteğini bulmak için bu müşteri listelerinin kesişimini alır.



**Arama yaklaşımı:**



Derinlik öncelikli (depth-first search) yapar.



Apriori gibi veri tabanını defalarca taramaz, sadece kümeler arası kesişim işlemi yapar.



A**vantajı:**



Daha hızlıdır, özellikle büyük veri setlerinde ve sık itemset bulmada etkilidir.



**Dezavantajı:**



Çok büyük müşteri listeleri olduğunda kesişim işlemleri pahalı olabilir.



| Özellik              | Apriori                            | Eclat                                    |

| -------------------- | ---------------------------------- | ---------------------------------------- |

| \*\*Veri yapısı\*\*      | Yatay (transaction list)           | Dikey (ürün → müşteri listesi)           |

| \*\*Arama yöntemi\*\*    | Breadth-first (genişlik öncelikli) | Depth-first (derinlik öncelikli)         |

| \*\*Destek hesaplama\*\* | Veri tabanını tekrar tekrar tarar  | Müşteri ID kümelerinin kesişimiyle       |

| \*\*Hız\*\*              | Daha yavaş (çok tarama yapar)      | Daha hızlı (daha az tarama)              |

| \*\*Kullanım alanı\*\*   | Küçük/orta veri setleri            | Büyük veri setleri, sık itemset çıkarımı |



