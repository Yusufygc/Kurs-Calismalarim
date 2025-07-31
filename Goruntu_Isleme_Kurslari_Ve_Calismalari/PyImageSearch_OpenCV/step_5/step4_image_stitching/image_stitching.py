# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
	help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,
	help="path to the output image")
ap.add_argument("-c", "--crop", type=int, default=0,
	help="whether to crop out largest rectangular region") # 0 = no crop, 1 = crop terminalde bir verdiğimiz zaman kırpma gerçekleşecek.
args = vars(ap.parse_args())

# grab the paths to the input images and initialize our images list
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []

# loop over the image paths, load each one, and add them to our
# images to stich list
for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)
	
# initialize OpenCV's image sticher object and then perform the image
# stitching
print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

# if the status is '0', then OpenCV successfully performed image
# stitching
if status == 0:
	# check to see if we supposed to crop out the largest rectangular region from the stitched image
    # birleştirdiğimiz görüntüden en büyük dikdörtgeni kırpıp kırpamayacağımızı kontrol ediyoruz.
	if args["crop"] > 0:
		# create a 10 pixel border surrounding the stitched image
		print("[INFO] cropping...")
		stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10,
			cv2.BORDER_CONSTANT, (0, 0, 0))  # tüm panorama taslağının dış hatlarını
		# bulabilmemizi sağlamak için birleştirilmiş görüntümüzün (43 ve 44. Satır)
        #  her tarafına 10 piksellik bir kenarlık ekleyeceğiz.

		# convert the stitched image to grayscale and threshold it
		# such that all pixels greater than zero are set to 255
		# (foreground) while all others remain 0 (background)
		gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
		thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
		"""
        Eşikli görüntümüz göz önüne alındığında, kontur çıkarma işlemini uygulayabilir, en büyük konturun sınırlayıcı kutusunu hesaplayabilir (yani, panoramanın anahattı) ve sınırlayıcı kutuyu çizebiliriz:
	    """
		# find all external contours in the threshold image then find
		# the *largest* contour which will be the contour/outline of
		# the stitched image
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE) # dış hatları buluyoruz.
		cnts = imutils.grab_contours(cnts) # konturları yakalıyoruz.
		c = max(cnts, key=cv2.contourArea) # en büyük konturu buluyoruz. 
		
		# allocate memory for the mask which will contain the
		# rectangular bounding box of the stitched image region
		mask = np.zeros(thresh.shape, dtype="uint8") # maske oluşturuyoruz.
		(x, y, w, h) = cv2.boundingRect(c) # en büyük konturun sınırlayıcı kutusunu hesaplıyoruz.
		cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1) # sınırlayıcı kutuyu çiziyoruz.

        # create two copies of the mask: one to serve as our actual
		# minimum rectangular region and another to serve as a counter
		# for how many pixels need to be removed to form the minimum
		# rectangular region
		minRect = mask.copy() # minimum dikdörtgen bölgeyi oluşturmak için kullanacağımız maske
		sub = mask.copy() 
		
		# keep looping until there are no non-zero pixels left in the
		# subtracted image
		while cv2.countNonZero(sub) > 0: # sub görüntüsünde 0 olmayan piksel kalmayana kadar döngüyü sürdürüyoruz.
			# erode the minimum rectangular mask and then subtract
			# the thresholded image from the minimum rectangular mask
			# so we can count if there are any non-zero pixels left
			minRect = cv2.erode(minRect, None) # minimum dikdörtgen bölgeyi erode ediyoruz. erode= aşındırma morfolojik işlemi
			sub = cv2.subtract(minRect, thresh) # eşikli görüntüden minimum dikdörtgen bölgeyi çıkarıyoruz.
			"""
			İlk maske olan minMask , panoramanın iç kısmına sığana kadar yavaşça küçültülecektir
			İkinci maske olan sub , minMask boyutunu küçültmeye devam etmemiz gerekip gerekmediğini belirlemek için kullanılacaktır.
			
			MinRect boyutunun, alt kısımda hiç ön plan pikseli kalmayana kadar kademeli olarak nasıl küçültüldüğüne dikkat edin — bu noktada, panoramanın en büyük dikdörtgen bölgesine sığabilecek en küçük dikdörtgen maskeyi bulduğumuzu biliyoruz.
			    
	        """ 
		"""
	    Minimum iç dikdörtgen göz önüne alındığında, tekrar konturları bulabilir ve sınırlayıcı kutuyu hesaplayabiliriz, ancak bu sefer ROI'yi birleştirilmiş görüntüden basitçe çıkaracağız:
        """	
		# find contours in the minimum rectangular mask and then
		# extract the bounding box (x, y)-coordinates
		cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE) # minimum dikdörtgen bölgeyi buluyoruz.
		cnts = imutils.grab_contours(cnts) # konturları yakalıyoruz.
		c = max(cnts, key=cv2.contourArea) # en büyük konturu buluyoruz.
		(x, y, w, h) = cv2.boundingRect(c) # en büyük konturun sınırlayıcı kutusunu hesaplıyoruz.
		
		# use the bounding box coordinates to extract the our final
		# stitched image
		stitched = stitched[y:y + h, x:x + w] # sınırlayıcı kutudan son panoramik görüntüyü çıkarıyoruz.
		
	# write the output stitched image to disk
	cv2.imwrite(args["output"], stitched)
	
	# display the output stitched image to our screen
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)
	
# otherwise the stitching failed, likely due to not enough keypoints)
# being detected
else: # eğer birleştirme başarısız olursa
	print("[INFO] image stitching failed ({})".format(status))