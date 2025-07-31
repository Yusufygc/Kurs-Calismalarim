
import cv2


cap = cv2.VideoCapture(0)
# fonksiyonun içine verilecek parametre hangi donanımı ya da 
# halihaızrda bulunan bir vidoyu mu kullanacağımızı belirtir
# videonun adresini vererek hazır video kullanabiliriz

while True:
    ret, frame = cap.read()# frame leri doğru okumuşsa ret true değer döndürür
    frame = cv2.flip(frame,1)# görüntüyü istediğimiz eksene göre yansıtır
    # ilki görüntü kaynağı,ikincisi eksendir 1 y ye karşılık gelir
    cv2.imshow("Webcam",frame) # ilki pencerenin adı ,ikincisi görüntünün alındığı kaynak
    cv2.waitKey(30) # içerdeki değer ne kadar küçülürse framein ekranda kalma süresi o kadar azalır
    
    
    if 0xFF == ord("q"):
        break
    # q ya basınca videonun kapatılmasını sağlar

cap.release() #videoyu kapatıp işlem yapmaya devam etmemizi sağlar
cv2.destroyAllWindows()


