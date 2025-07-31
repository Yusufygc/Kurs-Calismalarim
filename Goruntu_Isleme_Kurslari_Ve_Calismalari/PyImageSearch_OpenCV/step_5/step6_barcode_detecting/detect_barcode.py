# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "path to the image file")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute the Scharr gradient magnitude representation of the images
# in both the x and y direction using OpenCV 2.4
ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)  
gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)  
"""
Ardından, Satır 19-21'de yatay ve dikey yönlerde gri tonlamalı 
görüntünün gradyan büyüklük temsilini oluşturmak için 
Scharr operatörünü (ksize = -1 kullanılarak belirtilir) kullanırız.
"""
# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
"""
Oradan, Scharr operatörünün y-gradyanını Satır 28 ve 29'teki
Scharr operatörünün x-gradyanından çıkarırız. Bu çıkarma işlemini
gerçekleştirerek görüntünün yüksek yatay gradyanlara ve düşük
dikey gradyanlara sahip bölgeleri kalır.
"""

# blur and threshold the image
blurred = cv2.blur(gradient, (9, 9)) # 9x9'luk bir bulanıklık uyguluyoruz
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY) # 225 değerinden büyük olanları beyaz(255), küçük olanları siyah(0) yapıyoruz 
"""
barkodun dikey çubukları arasında boşluklar bulunmaktadır. Bu boşlukları kapatmak ve algoritmamızın barkodun "blob" benzeri bölgesini algılamasını kolaylaştırmak için bazı temel morfolojik işlemleri gerçekleştirmemiz gerekecek (blob = küme, küme benzeri bölge)
"""

# construct a closing kernel and apply it to the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7)) 
# MORPH_RECT: dikdörtgen şeklinde boyutu 21x7 lik kernel oluşturuyoruz
# Bu çekirdek, yükseklikten daha büyük
# bir genişliğe sahiptir, böylece barkodun 
# dikey şeritleri arasındaki boşlukları kapatmamızı sağlar.
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# morfolojik işlemimizi, çekirdeğimizi eşiklenmiş görüntümüze uygularız, böylece çubuklar arasındaki boşlukları kapatabiliriz 

# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations = 4) # 4 kez erozyon uyguluyoruz
closed = cv2.dilate(closed, None, iterations = 4) # 4 kez genişletiyoruz
"""
Aşınma, görüntüdeki beyaz pikselleri "aşındırarak" 
küçük lekeleri ortadan kaldırırken, 
genişleme kalan beyaz pikselleri "genişletecektir".
Aşınma sırasında küçük lekeler çıkarılmışsa, 
genişleme sırasında tekrar ortaya çıkmazlar.
Aşındırma ve genişletme serimizden sonra,
küçük lekelerin başarıyla kaldırıldığını 
ve barkod bölgesiyle kaldığımızı görebilirsiniz.
"""

# find the contours in the thresholded image, then sort the contours
# by their area, keeping only the largest one
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE) # dış kenarları buluyoruz
cnts = imutils.grab_contours(cnts) # konturları yakalıyoruz
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0] # konturları alanlarına göre sıralıyoruz ve en büyük olanı alıyoruz

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c) # en küçük dikdörtgeni buluyoruz
box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect) # dikdörtgenin köşe noktalarını buluyoruz
box = np.int0(box) # köşe noktalarını int değerlerine çeviriyoruz

# draw a bounding box arounded the detected barcode and display the
# image
cv2.drawContours(image, [box], -1, (0, 255, 0), 3) 
cv2.imshow("Image", image)
cv2.waitKey(0)

