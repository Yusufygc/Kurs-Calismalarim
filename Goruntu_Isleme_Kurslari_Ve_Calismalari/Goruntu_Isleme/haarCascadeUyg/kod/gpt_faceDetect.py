import cv2

# CascadeClassifier yükleyin (OpenCV'nin önceden eğitilmiş bir yüz tanıma modeli)
face_cascade = cv2.CascadeClassifier("C:\\Users\\TUF Dash F15\\Desktop\\KODLAR\\IMAGE_PROCESSING\\Goruntu_Isleme\\haarCascadeUyg\\haarCascade\\frontalface.xml")

# Kamerayı başlatın
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare alın
    ret, frame = cap.read()

    # Gri tonlamaya dönüştürün (yüz tanıma için daha iyi)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Tespit edilen yüzleri işaretle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Pencereye kameradan alınan kareyi ve yüzleri çizin
    cv2.imshow('Face Detection', frame)

    # 'q' tuşuna basılınca döngüyü sonlandırın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırakın ve pencereyi kapatın
cap.release()
cv2.destroyAllWindows()
