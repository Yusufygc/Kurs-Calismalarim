"""
Adım 1 = Termostattaki LCD'yi yerelleştirelim. Bu, plastik kabuk ile LCD arasında yeterli kontrast olduğundan, kenar algılama kullanılarak yapabiliriz.

Adım 2 = Bir giriş kenar haritası verildiğinde, konturları bulabilir ve dikdörtgen şekilli ana hatları arayabiliriz - en büyük dikdörtgen bölge LCD'ye karşılık gelmelidir. Bir perspektif dönüşümü bize LCD'nin güzel bir şekilde çıkarılmasını sağlayacak.

Adım 3 = Rakam bölgelerini seçelim. LCD'nin kendisine sahip olduğumuzda, rakamları çıkarmaya odaklanabiliriz. Rakam bölgeleri ile LCD'nin arka planı arasında kontrast varmış gibi göründüğünden, eşikleme ve morfolojik işlemler ile bunu başarabiliriz.

Adım 4 = Rakamları tanımlayalım. OpenCV ile gerçek basamakları tanımak, basamak ROI'sini yedi bölüme ayırmayı içermektir. Oradan, belirli bir segmentin "açık" veya "kapalı" olup olmadığını belirlemek için eşikli görüntüye piksel sayımı uygulayabiliriz.
"""
# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

# define the dictionary of digit segments so we can identify
# each digit on the thermostat
DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0, 
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 1, 0): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9
} # 0-9 arası rakamların 7 segmentlerini tanımladık
# 1 ler segmentlerin açık olduğu yerler 0 lar kapalı olduğu yerlerdir

# load the example image
image = cv2.imread("C:\\Users\\TUF Dash F15\\Desktop\\pyimagesearch\\step_5\\step5_recognizing_digits\\src\\termo.png")

# pre-process the image by resizing it, converting it to
# graycale, blurring it, and computing an edge map
image = imutils.resize(image, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)

# find contours in the edge map, then sort them by their
# size in descending order
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None

# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True) # konturun uzunluğunu buluyoruz
	approx = cv2.approxPolyDP(c, 0.02 * peri, True) # konturun köşelerini buluyoruz

	# if the contour has four vertices, then we have found
	# the thermostat display
	if len(approx) == 4:
		displayCnt = approx
		break

# extract the thermostat display, apply a perspective transform
# to it
warped = four_point_transform(gray, displayCnt.reshape(4, 2)) 
output = four_point_transform(image, displayCnt.reshape(4, 2))
# Dört köşeyi elde ettikten sonra,
# LCD'yi dört noktalı bir perspektif 
# dönüşümü yoluyla çıkarabiliriz:

# threshold the warped image, then apply a series of morphological
# operations to cleanup the thresholded image
thresh = cv2.threshold(warped, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] # eşikleme işlemi
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5)) # morfolojik işlemler için kernel oluşturduk 
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) # morfolojik işlem uyguladık 
""" 
Basamakların kendilerini elde etmek, karanlık bölgeleri (yani basamakları) 
daha açık arka plana (yani LCD ekranın arka planına) karşı ortaya çıkarmak 
için çarpık görüntüyü (Satır 72 ve 73) eşiklememiz gerekir.
Ardından, eşikli görüntüyü temizlemek için bir dizi morfolojik işlem uyguluyoruz (Satır 74 ve 75)
Artık güzel bir parçalanmış görüntümüz olduğuna göre, bir kez daha 
kontur filtreleme uygulamamız gerekiyor, ancak bu sefer gerçek rakamları arıyoruz.
"""
# find contours in the thresholded image, then initialize the
# digit contours lists
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE) # konturları bulduk
cnts = imutils.grab_contours(cnts) # konturları yakaladık
digitCnts = [] # rakamların konturlarını tutacağımız listeyi oluşturduk

# loop over the digit area candidates
for c in cnts:
	# compute the bounding box of the contour
	(x, y, w, h) = cv2.boundingRect(c) # konturun koordinatlarını aldık
	# if the contour is sufficiently large, it must be a digit
	if w >= 15 and (h >= 30 and h <= 40): # konturun genişliği ve yüksekliğini kontrol ettik
		digitCnts.append(c) # eğer koşullar sağlanıyorsa rakam konturlarını listeye ekledik

"""
Uygun genişlik ve yükseklik kısıtlamalarının belirlenmesi, 
birkaç tur deneme yanılma gerektirir. Konturların her birinin üzerinden geçmenizi,
 ayrı ayrı çizmenizi ve boyutlarını incelememiz daha faydalı olur. 
 Bu işlemi yapmak, basamak kontur özellikleri arasında ortak noktalar bulabilmemizi sağlar.
"""

# sort the contours from left-to-right, then initialize the
# actual digits themselves
digitCnts = contours.sort_contours(digitCnts,
	method="left-to-right")[0]
digits = []

# loop over each of the digits
for c in digitCnts:
	# extract the digit ROI
	(x, y, w, h) = cv2.boundingRect(c)
	roi = thresh[y:y + h, x:x + w]

	# compute the width and height of each of the 7 segments
	# we are going to examine
	(roiH, roiW) = roi.shape 
	(dW, dH) = (int(roiW * 0.25), int(roiH * 0.15)) 
	dHC = int(roiH * 0.05) 
	# ROI boyutlarına dayalı olarak 
	# her segmentin yaklaşık genişliğini ve yüksekliğini hesapladık.

	# define the set of 7 segments
	segments = [
		((0, 0), (w, dH)),	# top
		((0, 0), (dW, h // 2)),	# top-left
		((w - dW, 0), (w, h // 2)),	# top-right
		((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
		((0, h // 2), (dW, h)),	# bottom-left
		((w - dW, h // 2), (w, h)),	# bottom-right
		((0, h - dH), (w, h))	# bottom
	] # 7 segmentin koordinatlarını belirledik(dijital değerde bir sayı max 7 segmentten oluşur)) 
	on = [0] * len(segments) # 7 segmentin açık olup olmadığını tutacağımız listeyi oluşturduk (0 lar kapalı 1 ler açık olduğunu ifade eder)

	# loop over the segments
	for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
		# extract the segment ROI, count the total number of
		# thresholded pixels in the segment, and then compute
		# the area of the segment
		segROI = roi[yA:yB, xA:xB] # segmentin ROI sini aldık
		total = cv2.countNonZero(segROI) # segmentin içindeki sıfır 
		# olmayan piksel sayısını bulduk (segmentteki "açık" olan piksel sayısı)
		area = (xB - xA) * (yB - yA)

		# if the total number of non-zero pixels is greater than
		# 50% of the area, mark the segment as "on"
		if total / float(area) > 0.5: 
			on[i]= 1
			# Sıfır olmayan piksellerin segmentin toplam alanına
			# oranı %50'den büyükse, segmentin "açık" olduğunu
			# varsayabilir ve listemizi buna göre güncelleyebiliriz.

	# lookup the digit and draw it on the image
	digit = DIGITS_LOOKUP[tuple(on)]
	digits.append(digit)
	cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
	cv2.putText(output, str(digit), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
	
	"""
	Yedi parça üzerinde döngü yaptıktan sonra,
	rakamın kendisini elde etmek için açık listesini 
	DIGITS_LOOKUP'a iletebiliriz.
	Daha sonra rakamın etrafına bir sınırlayıcı kutu
	çizeriz ve rakamı çıktı görüntüsünde gösteririz.
	"""

# display the digits
print(u"{}{}.{} \u00b0C".format(*digits)) # derece işareti için \u00b0C kullandık
cv2.imshow("Input", image)
cv2.imshow("Output", output)
cv2.waitKey(0)