# import the necessary packages
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

class ColorLabeler:
	def __init__(self):
		# initialize the colors dictionary, containing the color
		# name as the key and the RGB tuple as the value
		colors = OrderedDict({
			"red": (255, 0, 0),
			"green": (0, 255, 0),
			"blue": (0, 0, 255)})
		
		# allocate memory for the L*a*b* image, then initialize
		# the color names list (allocate = ayırmak, tahsis etmek)
		self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
		self.colorNames = []
		
		# loop over the colors dictionary
		for (i, (name, rgb)) in enumerate(colors.items()):
			# update the L*a*b* array and the color names list
			self.lab[i] = rgb
			self.colorNames.append(name)
			
		# convert the L*a*b* array from the RGB color space
		# to L*a*b*
		self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)
		"""
        Lab* renk uzayını neden RGB veya HSV yerine kullanıyoruz?

        Belirli bir renge sahip olduğunu düşündüğümüz görüntü bölgelerini etiketlemek ve işaretleme yapabilmek için, bilinen renklerimizin (yani lab dizisinin) veri kümemizle ve belirli bir görüntü bölgesinin ortalama renk değerleri arasındaki Öklidyen mesafesini hesaplayacağız.
	
        Öklidyen mesafeyi en küçükleyen renk, renk tanımlaması için seçilecektir.
        """
	def label(self, image, c):
		# construct a mask for the contour, then compute the
		# average L*a*b* value for the masked region
		mask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)
		mask = cv2.erode(mask, None, iterations=2)
		mean = cv2.mean(image, mask=mask)[:3]
		
		# initialize the minimum distance found thus far
		# şimdiye kadar bulunan minimum mesafeyi başlatalım.
		minDist = (np.inf, None)
		
		# loop over the known L*a*b* color values
		for (i, row) in enumerate(self.lab):
			# compute the distance between the current L*a*b*
			# color value and the mean of the image
			# şu anki L*a*b* renk değeri ile
			# görüntünün ortalaması arasındaki mesafeyi hesaplayalım.
			d = dist.euclidean(row[0], mean)
			
			# if the distance is smaller than the current distance,
			# then update the bookkeeping variable
			if d < minDist[0]:
				minDist = (d, i)
				
		# return the name of the color with the smallest distance
		# en küçük mesafeye sahip rengin adını döndürür
		return self.colorNames[minDist[1]]