# import the necessary packages
import imutils
import cv2

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
# Giriş resmini yükleyip boyutlarını göstermek için resimlerin
# çok boyutlu NumPy dizileri olarak temsil edildiğini unutmayın. 
# Bu temsile göre resimler, satır sayısı (yükseklik) x sütun sayısı (genişlik)
# x kanal sayısı (derinlik) şeklinde bir yapıya sahiptir.
image = cv2.imread("jp.jpg") # cmd step_3 olmadan çalıştırıyor vsc step_3\\ olmadan çalıştırmıyor.

# resmin ölçülerini değişkenlere atadık.
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
# x=50, y=100 konumunda bulunan RGB pikseline erişiyoruz.
# OpenCV, resimleri RGB yerine BGR sırasında saklar.unutmayın
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
# Giriş resmindeki x = 320, y = 60'tan başlayarak x = 420, y = 160'ta sona eren
# 100x100 piksel kare ROI (İlgi Bölgesi) çıkarıyoruz.
roi = image[60:160, 320:420] # image[startY:endY, startX:endX]

cv2.imshow("ROI", roi)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# resize the image to 200x200px, ignoring aspect ratio
# en boy oranını gözardı ederek resmi 200x200 piksele yeniden boyutlandırıyoruz.
resized = cv2.resize(image, (200, 200))

cv2.imshow("Fixed Resizing", resized)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
# manuel olarak en boy oranını hesaplamak ızdırap olabilir,
# bunun yerine imutils kütüphanesini kullanalım
resized1 = imutils.resize(image, width=300)

cv2.imshow("Imutils Resize", resized1)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
# en/boy oranını bozmadan sabit bir yeniden boyutlandırma yaparak
# genişliği 300 piksele yeniden boyutlandıralım, 
# ancak yeni yüksekliği oranı koruyarak hesaplayalım.
# aslında üstteki işlemleri birleştirip manuel yapıyoruz diye düşünebiliriz.
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)

cv2.imshow("Aspect Ratio Resize", resized)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
# Önce resim merkezini hesaplayarak, ardından dönüş matrisini oluşturarak
# ve son olarak da afin warp uygulayarak OpenCV'yi kullanarak bir resmi
# saat yönünde 45 derece döndürelim.
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("OpenCV Rotation", rotated)

"""
Affine dönüşümlerinden bahsetmeden önce, Öklid dönüşümlerinin ne olduğunu öğrenelim. Öklid dönüşümleri uzunluk ve açı ölçülerini koruyan bir tür geometrik dönüşümdür. Geometrik bir şekil alır, öklid dönüşümünü uygularsak şekil değişmeyecektir. Bu işlem sonucu şekil, döndürülmüş, kaydırılmış gibi görünebilir, ancak temel yapı değişmeyecektir. Teknik olarak, çizgiler çizgiler halinde kalacak, düzlem düzlem kalacak, kareler kareler kalacak ve daireler daireler kalacak.

Affine dönüşümlerine geri dönersek, Öklid dönüşümlerinin genelleşmiş hali olduklarını söyleyebiliriz. Affine dönüşümleri altında, çizgiler çizgiler halinde kalacaktır, ancak kareler, dikdörtgenler veya paralelkenarlar haline gelebilir. Temel olarak, affine dönüşümler uzunlukları ve açıları korumaz.

Bir affine transformation matrix oluşturmak istiyorsak, öncelikle kontrol noktalarını belirlememiz gerekir. Bu noktaları tanımladıktan sonra, hangi noktalara mapped olacaklarına karar vermemiz gerekir. Örnek olarak input ve output resimlerinden 3 nokta alacağız.
"""
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# rotation can also be easily accomplished via imutils with less code
# rotation daha az ızdırapla imutils ile de kolayca gerçekleştirilebilir.
rotated1 = imutils.rotate(image, -45)

cv2.imshow("Imutils Rotation", rotated1)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help us out
# Opencv rotatiodan sonra resim kırpılmış bozulmuş umursamaz bana dokunmayan yılan bin yaşasın der.
# ama yine imutils kütüphanesinden yardım alarak resmimizi koruyabiliriz.
rotated2 = imutils.rotate_bound(image, 45)

cv2.imshow("Imutils Bound Rotation", rotated2)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
# yüksek frekanslı gürültüyü azaltırken resme 
# 11x11 çekirdekli bir Gaussian bulanıklığı uygulayalım.
blurred = cv2.GaussianBlur(image, (11, 11), 0)

cv2.imshow("Blurred", blurred)

# Daha büyük çekirdekler daha bulanık bir görüntü verir.
# Daha küçük çekirdekler daha az bulanık görüntüler oluşturacaktır.
# çekirdeğin boyutu tek sayı olmalıdır.
# çekirdek=kernel

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# draw a 2px thick red rectangle surrounding the face
# belirlediğimiz kafanın etrafına 2px kalınlığında kırmızı bir dikdörtgen çizelim.
# istediğimiz kafaya ,yere ,konuma çizebiiriz
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)

cv2.imshow("Rectangle", output)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
# x=300,y=150 merkezindeki resimde mavi 20px (doldurulmuş) çember çizelim.
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1) # -1 çemberi doldurur/ -1 fills the circle.

cv2.imshow("Circle", output)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
# x=60,y=20'den x=400,y=200'e 5px kalınlığında kırmızı bir çizgi çizelim.
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)

cv2.imshow("Line", output)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# draw green text on the image
# resim üzerine yeşil metin çizelim. 
# yazı, renk ,kalınlık ,font ,yazı boyutu keyfimizin kahyasına kalmış.
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)


#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
# görüntüyü gösterelim.

cv2.imshow("Image", image)
cv2.waitKey(0)