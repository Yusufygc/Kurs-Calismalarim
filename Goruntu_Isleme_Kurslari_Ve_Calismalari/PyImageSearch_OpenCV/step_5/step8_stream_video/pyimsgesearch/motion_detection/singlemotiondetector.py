# import the necessary packages
import numpy as np
import imutils
import cv2

class SingleMotionDetector:
	def __init__(self, accumWeight=0.5):
		# store the accumulated weight factor
		self.accumWeight = accumWeight # 0.5 is the default value  accumWeight is = 0.5 means that the background model will take 50% of the current frame and 50% of the previous frame into account when building the background model.(arka plan modeli oluşturulurken mevcut çerçevenin %50'sini ve önceki çerçevenin %50'sini dikkate alacaktır.)AccumWeight ne kadar büyük olursa, ağırlıklı ortalama toplanırken arka plan (bg) o kadar az hesaba katılır.Tersine, AccumWeight ne kadar küçükse, ortalama hesaplanırken arka plan bg o kadar fazla dikkate alınacaktır.  
		# initialize the background model
		self.bg = None # background model is None at the beginning
		
        
	def update(self, image):
		# if the background model is None, initialize it
		if self.bg is None:
			self.bg = image.copy().astype("float")
			return
		
		# update the background model by accumulating the weighted
		# average
		cv2.accumulateWeighted(image, self.bg, self.accumWeight)
		

	def detect(self, image, tVal=25):
		# tVal = Belirli bir pikseli “hareket” olarak işaretlemek için kullanılan eşik değeri.
		# compute the absolute difference between the background model
		# and the image passed in, then threshold the delta image
		delta = cv2.absdiff(self.bg.astype("uint8"), image) # delta, arka plan modeli ile iletilen görüntü arasındaki farktır.
		thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1] # delta görüntüsünü eşikleyerek, hareketi gösteren bir maske oluştururuz. Bu maske, hareketi gösteren beyaz pikseller ve hareketsiz pikselleri gösteren siyah pikseller içerir.
		
		# perform a series of erosions and dilations to remove small
		# blobs
		thresh = cv2.erode(thresh, None, iterations=2) # küçük parçacıkları kaldırmak için erozyon ve genişletme işlemleri yapılır.
		thresh = cv2.dilate(thresh, None, iterations=2) 
		
		# find contours in the thresholded image and initialize the
		# minimum and maximum bounding box regions for motion
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE) # eşiklenmiş görüntüdeki konturları buluruz.
		cnts = imutils.grab_contours(cnts) 
		(minX, minY) = (np.inf, np.inf) # minX, minY, maxX, maxY, en küçük ve en büyük x ve y koordinatlarını tutar.
		(maxX, maxY) = (-np.inf, -np.inf)  
		# Herhangi bir hareketin bulunduğu konumu takip etmek için iki defter tutma değişkeni seti başlatırız (Satır 42 ve 43). Bu değişkenler, bize hareketin nerede gerçekleştiğini söyleyecek olan “sınırlayıcı kutuyu” oluşturacaktır.

        # Son adım, bu değişkenleri doldurmaktır (tabii ki çerçevede hareket olması koşuluyla)

		# if no contours were found, return None
		if len(cnts) == 0:
			return None
		
		# otherwise, loop over the contours
		for c in cnts:
			# compute the bounding box of the contour and use it to
			# update the minimum and maximum bounding box regions
			(x, y, w, h) = cv2.boundingRect(c) # Konturun sınırlayıcı kutusunu hesaplarız ve ardından minimum ve maksimum sınırlayıcı kutu bölgelerini güncellemek için kullanırız.
			(minX, minY) = (min(minX, x), min(minY, y)) 
			(maxX, maxY) = (max(maxX, x + w), max(maxY, y + h)) 
			# Her kontur için sınırlayıcı kutuyu hesaplıyoruz ve ardından tüm hareketin onu gerçekleştirdiği minimum ve maksimum (x, y) koordinatlarını bularak muhasebe değişkenlerimizi (Satır 52-58) güncelliyoruz.

		# otherwise, return a tuple of the thresholded image along
		# with bounding box
		return (thresh, (minX, minY, maxX, maxY))