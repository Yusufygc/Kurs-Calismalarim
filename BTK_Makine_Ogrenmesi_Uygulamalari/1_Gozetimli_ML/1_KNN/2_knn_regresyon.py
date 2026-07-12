"""
Kodun genel çalışma mantığı
40 adet rastgele veri oluşturulur.
Bu verilerin sinüs fonksiyonu alınarak hedef değer (y) elde edilir.
Gerçek hayattaki verileri taklit etmek için bazı noktalara gürültü (noise) eklenir.
KNeighborsRegressor modeli iki farklı ağırlık yöntemiyle eğitilir:
uniform: En yakın 5 komşunun her biri aynı öneme sahiptir.
distance: Yakındaki komşular daha fazla etkiye sahiptir.
0–5 aralığındaki 500 noktada tahmin yapılır.
Son olarak eğitim verileri ve tahmin eğrileri iki ayrı grafikte karşılaştırılır.

Bu örnek, KNN Regresyonunda weights="uniform" ile weights="distance" seçeneklerinin tahmin eğrisini nasıl değiştirdiğini görselleştirmek için hazırlanmıştır.

"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

# -----------------------------
# Eğitim verisinin oluşturulması
# -----------------------------

# 0 ile 5 arasında rastgele 40 adet sayı üret
# sort() ile küçükten büyüğe sırala
X = np.sort(5 * np.random.rand(40, 1), axis=0)

# X değerlerinin sinüsünü al
# ravel() -> (40,1) boyutundaki diziyi (40,) haline getirir
# Scikit-Learn hedef değişkeni (y) için genellikle tek boyutlu dizi ister.
y = np.sin(X).ravel()

# Temiz veriyi görmek istersen:
# plt.scatter(X, y)

# -----------------------------
# Veriye gürültü (noise) ekleme
# -----------------------------

# Her 5. elemana rastgele bir hata ekleniyor.
# Böylece gerçek hayattaki ölçüm hataları taklit edilmiş oluyor.
#
# y[::5]   -> 0,5,10,15,... indekslerini seçer.
# np.random.rand(8) -> 8 adet rastgele sayı üretir.
# (0.5 - rand) -> -0.5 ile +0.5 arasında rastgele değerler oluşturur.
y[::5] += 1 * (0.5 - np.random.rand(8))

# Gürültülü veriyi görmek istersen:
# plt.scatter(X, y)

# -----------------------------
# Tahmin yapılacak test verisi
# -----------------------------

# 0 ile 5 arasında 500 eşit nokta oluştur.
# Bu noktalar modelin tahmin eğrisini çizmek için kullanılacak.
T = np.linspace(0, 5, 500)[:, np.newaxis]

# -----------------------------
# İki farklı ağırlık yöntemi denenecek
# -----------------------------
#
# uniform : Komşuların hepsi eşit ağırlığa sahip.
# distance: Yakın komşular daha fazla ağırlık alır.
#
for i, weight in enumerate(["uniform", "distance"]):

    # KNN Regresyon modeli oluştur
    # n_neighbors = 5 -> En yakın 5 komşu kullanılacak.
    knn = KNeighborsRegressor(
        n_neighbors=5,
        weights=weight
    )

    # Modeli eğit ve test noktaları için tahmin yap
    y_pred = knn.fit(X, y).predict(T)

    # -----------------------------
    # Grafik çizimi
    # -----------------------------

    # 2 satır, 1 sütunluk grafikte ilgili bölümü seç
    plt.subplot(2, 1, i + 1)

    # Eğitim verilerini göster
    plt.scatter(
        X,
        y,
        color="green",
        label="Training Data"
    )

    # Modelin tahmin eğrisini çiz
    plt.plot(
        T,
        y_pred,
        color="blue",
        label="Prediction"
    )

    # Eksenleri veriye göre otomatik ayarla
    plt.axis("tight")

    # Açıklama kutusu
    plt.legend()

    # Grafik başlığı
    plt.title(f"KNN Regressor (weights = {weight})")

# Grafikler arasında boşlukları otomatik ayarla
plt.tight_layout()

# Grafikleri ekrana göster
plt.show()