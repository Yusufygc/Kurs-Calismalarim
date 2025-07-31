"""
Step #1: Detect keypoints (DoG, Harris, etc.) and extract local invariant descriptors (SIFT, SURF, etc.) from the two input images.
Step #2: Match the descriptors between the two images.
Step #3: Use the RANSAC algorithm to estimate a homography matrix using our matched feature vectors.
Step #4: Apply a warping transformation using the homography matrix obtained from Step #3.

Adım #1: Anahtar noktaları (DoG, Harris, vb.) tespit edin ve iki giriş görüntüsünden yerel değişmez tanımlayıcıları (SIFT, SURF, vb.) çıkaralım.
Adım #2: İki resim arasındaki tanımlayıcıları eşleştirelim.
Adım #3: Eşleştirilmiş öznitelik vektörlerimizi kullanarak bir homografi matrisini tahmin etmek için RANSAC algoritmasını kullanalım.
Adım #4: Adım #3'ten elde edilen homografi matrisini kullanarak bir çarpıtma dönüşümü uygulayalım.

"""
# import the necessary packages
import numpy as np
import imutils
import cv2

class Stitcher:
	def __init__(self):
		# determine if we are using OpenCV v3.X
		self.isv3 = imutils.is_cv3(or_better=True)
		
	def stitch(self, images, ratio=0.75, reprojThresh=4.0,
		showMatches=False):
		"""
	    İsteğe bağlı olarak, özellikleri eşleştirirken David Lowe'un oran testi için kullanılan oran, RANSAC algoritmasının izin verdiği maksimum piksel "hareket alanı" olan reprojThresh ve son olarak bir boolean olan showMatches'ı sağlayabiliriz. anahtar nokta eşleşmelerinin görselleştirilmesinin gerekip gerekmediğini belirtmek için kullanılır.
	    """
		# unpack the images, then detect keypoints and extract
		# local invariant descriptors from them
		(imageB, imageA) = images # görüntülerin soldan sağa sıralanmasını bekliyoruz.
		# Bu sırayla sağlanmazsa kodumuz çalışmaya devam eder, 
        # ancak çıktı panoramamaız yalnızca bir görüntü içerir.
		(kpsA, featuresA) = self.detectAndDescribe(imageA) # görüntü A'dan anahtar noktaları ve özellikleri çıkarırız.
		(kpsB, featuresB) = self.detectAndDescribe(imageB) # görüntü B'den anahtar noktaları ve özellikleri çıkarırız.
		
		# match features between the two images
		M = self.matchKeypoints(kpsA, kpsB,
			featuresA, featuresB, ratio, reprojThresh) # iki görüntü arasındaki özellikleri eşleştiririz.
		
		# if the match is None, then there aren't enough matched
		# keypoints to create a panorama
		if M is None: # eşleşme yoksa, o zaman bir panoramik oluşturmak için yeterli eşleşen anahtar nokta yoktur.
			return None
		
		# otherwise, apply a perspective warp to stitch the images
		# together
		(matches, H, status) = M # eşleşmeler, H ve durum değişkenlerini çıkarırız.
		# H, görüntü A'yı görüntü B'ye kaydırmak için kullanılan homografi matrisidir.
        # status, eşleşmelerin başarılı olup olmadığını belirtir.
		""" 
		M değeri None olmadığı sürece, 47. satırda demetin içeriğini açarız, bize bir anahtar nokta eşleme listesi, RANSAC algoritmasından türetilmiş homografi matrisi H ve son olarak, RANSAC kullanılarak başarılı bir şekilde mekânsal olarak doğrulanan anahtar noktalarının hangileri olduğunu gösteren bir dizin listesi olan "status"ı elde ederiz.
		"""

		"""
		Homografi matrisi H'ye sahip olduğumuza göre, şimdi iki görüntüyü bir araya getirmeye hazırız. İlk olarak, cv2.warpPerspective işlevini üç argümanla çağırıyoruz: dönüştürmek istediğimiz görüntü (bu durumda sağdaki görüntü), 3 x 3 dönüşüm matrisi (H) ve son olarak çıktı görüntüsünün şekli. Çıktı görüntüsünün şeklini, her iki görüntünün genişliklerinin toplamını alarak ve ardından ikinci görüntünün yüksekliğini kullanarak elde ederiz.
		"""
		result = cv2.warpPerspective(imageA, H,
			(imageA.shape[1] + imageB.shape[1], imageA.shape[0])) 
		result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB 
		
		# check to see if the keypoint matches should be visualized
		if showMatches: # anahtar nokta eşleşmelerinin görselleştirilmesi gerekip gerekmediğini kontrol ederiz.
			vis = self.drawMatches(imageA, imageB, kpsA, kpsB, matches,
				status) # anahtar nokta eşleşmelerini görselleştiririz.
			
			# return a tuple of the stitched image and the
			# visualization
			return (result, vis) # dikilmiş(stitch) görüntü ve görselleştirme demetini döndürürüz.
		
		# return the stitched image
		return result
	

	def detectAndDescribe(self, image):
		# convert the image to grayscale
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# check to see if we are using OpenCV 3.X
		if self.isv3: # OpenCV 3.X kullanıp kullanmadığımızı kontrol ederiz.
			# detect and extract features from the image
			descriptor = cv2.xfeatures2d.SIFT_create() # SIFT öznitelik çıkarıcısını oluştururuz. SIFT = Scale-Invariant Feature Transform (Ölçekten Bağımsız Özellik Dönüşümü)
			(kps, features) = descriptor.detectAndCompute(image, None) # anahtar noktaları ve özellikleri çıkarırız.

		# otherwise, we are using OpenCV 2.4.X
		else:
			# detect keypoints in the image
			detector = cv2.FeatureDetector_create("SIFT")
			kps = detector.detect(gray)
			"""
			Bu noktadan sonra, SIFT özellik çıkarıcımızı yapılandırmak için `cv2.DescriptorExtractor_create`'i "SIFT" anahtar kelimesi kullanarak başlatmamız gerekmektedir. Çıkarıcı'nın `compute` yöntemini çağırmak, görüntüde tespit edilen her bir anahtar noktanın çevresini nicelendiren bir dizi özellik vektörü döndürür.
			"""
			# extract features from the image
			extractor = cv2.DescriptorExtractor_create("SIFT")
			(kps, features) = extractor.compute(gray, kps)

		# convert the keypoints from KeyPoint objects to NumPy
		# arrays
		kps = np.float32([kp.pt for kp in kps]) # anahtar noktalarını NumPy dizilerine dönüştürürüz.

		# return a tuple of keypoints and features
		return (kps, features)
	

	def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB,
		ratio, reprojThresh):
		"""
		`matchKeypoints` işlevi dört argüman gerektirir: İlk görüntü ile ilişkilendirilmiş anahtar noktalar ve özellik vektörleri, bunu takip eden ikinci görüntü ile ilişkilendirilmiş anahtar noktalar ve özellik vektörleri. Ayrıca David Lowe'un oran testi değişkeni ve RANSAC yeniden yansıtma eşiği de sağlanmalıdır.
		"""
		# compute the raw matches and initialize the list of actual
		# matches
		matcher = cv2.DescriptorMatcher_create("BruteForce") # brute-force matcher'ı oluştururuz. brute-force matcher, iki görüntü arasındaki tüm özellik vektörlerini karşılaştırır.
		rawMatches = matcher.knnMatch(featuresA, featuresB, 2) # özellik vektörlerini karşılaştırırız.
		"""
		knnMatch çağrısı, k=2'yi kullanarak iki özellik vektörü seti arasında k-NN eşleştirmesi gerçekleştirir (her bir özellik vektörü için ilk iki eşleşmenin döndürüldüğünü gösterir).En iyi eşleşme yerine ilk iki eşleşmeyi istememizin nedeni, hatalı pozitif eşleşme budaması için David Lowe'un oran testini uygulamamız gerektiğidir.
		"""
		matches = []

		# loop over the raw matches
		for m in rawMatches: # ham eşleşmeler üzerinde döngüye gireriz. 
			"""
			Yanlış pozitif eşleşmeleri elemek için, her biri için sırayla rawMatches'in üzerinden geçebiliriz (Satır 119) ve yüksek kaliteli özellik eşleştirmelerini belirlemek için Lowe'un oran testini uygulayabiliriz. Tipik olarak, Lowe'un oranı genellikle [0.7, 0.8] aralığındadır.
			"""
			# ensure the distance is within a certain ratio of each
			# other (i.e. Lowe's ratio test)
			if len(m) == 2 and m[0].distance < m[1].distance * ratio:
				matches.append((m[0].trainIdx, m[0].queryIdx))

		"""
		Lowe'un oran testini kullanarak eşleşmeleri elde ettikten sonra, 
		iki anahtar nokta grubu arasındaki homografiyi hesaplayabiliriz:
		
		"""
		# computing a homography requires at least 4 matches
		if len(matches) > 4:
			# construct the two sets of points
			ptsA = np.float32([kpsA[i] for (_, i) in matches])
			ptsB = np.float32([kpsB[i] for (i, _) in matches])

			# compute the homography between the two sets of points
			(H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,
				reprojThresh)
			
			# return the matches along with the homograpy matrix
			# and status of each matched point
			return (matches, H, status)
		
		# otherwise, no homograpy could be computed
		return None
		"""
		İki nokta kümesi arasında bir homografi hesaplamak, en az dört eşleşmelik bir başlangıç ​​kümesi gerektirir. Daha güvenilir bir homografi tahmini için, yalnızca dört eşleşen noktadan önemli ölçüde daha fazlasına sahip olmamız gerekir.
		"""
	
	"""
	Son olarak, Stitcher yöntemimizdeki son yöntem olan drawMatches, iki resim arasındaki anahtar nokta eşleşmelerini görselleştirmek için kullanılır:
	"""
	def drawMatches(self, imageA, imageB, kpsA, kpsB, matches, status):
		# initialize the output visualization image
		(hA, wA) = imageA.shape[:2]
		(hB, wB) = imageB.shape[:2]
		vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
		vis[0:hA, 0:wA] = imageA
		vis[0:hB, wA:] = imageB

		# loop over the matches
		for ((trainIdx, queryIdx), s) in zip(matches, status):
			# only process the match if the keypoint was successfully
			# matched
			if s == 1:
				# draw the match
				ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
				ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
				cv2.line(vis, ptA, ptB, (0, 255, 0), 1)

		# return the visualization
		return vis
		"""
		Bu yöntem, orijinal iki görüntüyü, her bir görüntüyle ilişkilendirilmiş anahtar noktalar kümesini, Lowe'un oran testini uyguladıktan sonra ilk eşleştirmeleri ve nihayet homografi hesaplamasından sağlanan durum listesini içermemizi gerektirir. Bu değişkenleri kullanarak, ilk görüntüdeki N anahtar noktasından ikinci görüntüdeki M anahtar noktasına düz bir çizgi çizerek "içeride" kalan anahtar noktalarını görselleştirebiliriz.
		"""	    
		