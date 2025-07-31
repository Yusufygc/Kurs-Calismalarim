"""
Along the way we’ll be:

- Learning how to convert images to grayscale with OpenCV
- Performing edge detection
- Thresholding a grayscale image
- Finding, counting, and drawing contours
- Conducting erosion and dilation
- Masking an image

Yol boyunca:

- OpenCV ile görüntüleri gri tonlamaya dönüştürmeyi öğrenmek
- Kenar algılama gerçekleştirme
- Gri tonlamalı bir görüntüyü eşikleme
- Konturları bulma, sayma ve çizme
- Erozyon ve dilatasyon yapmak
- Bir görüntüyü maskeleme

işlemlerini öğreneceğiz.

terminalde çalıştırmak için ---> python opencv_tutorial_02.py --image tetris.png
"""

# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# convert the image to grayscale
# görüntüyü gri tonlamaya dönüştürme
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# applying edge detection we can find the outlines of objects in images
# kenar algılama uygulayarak görüntülerdeki nesnelerin ana hatlarını bulabiliriz
edged = cv2.Canny(gray, 30, 150)
# minVal : A minimum threshold, in our case 30 .
# (Bizim durumumuzda minimum eşik 30) .
# maxVal : The maximum threshold which is 150 in our example.
# (Bizim durumumuzda minimum eşik 150).
cv2.imshow("Edged", edged)
cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Thresholding can help us to remove lighter or darker regions and contours of images.
# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image

# Eşik değeri belirleyerek, görüntüdeki daha açık veya daha koyu bölgeleri ve konturları çıkarabiliriz. 
# Görüntüyü eşikleyerek, tüm piksel değerlerini 225'ten küçük olanları 255'e (beyaz; ön plan) 
# ve 225'e eşit veya büyük olanları 255'e (siyah; arka plan) ayarlayarak görüntüyü segmente edebiliriz.
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Detecting and drawing contours // Konturları algılama ve çizme

# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
# eşiklenmiş görüntünün ön plan nesnelerinin konturlarını 
# (yani ana hatlarını) bulalım
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

# loop over the contours
for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	# çıktı görüntüsüne her konturu 3 piksel kalınlığında mor bir çerçeve ile çizelim,
	# ardından çıktı konturlarını tek tek görüntüleyelim
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contours", output)
	cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
# bulduğumuz nesnelerin sayısını gösterelim
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Erosions and dilations can also be used to remove noise
# Erozyonlar ve genişlemeler de gürültüyü gidermek için kullanılabilir.
# Ön plan nesnelerinin boyutunu küçültmek için, 
# birkaç yineleme verildiğinde pikselleri aşındırabiliriz:

# we apply erosions to reduce the size of foreground objects 
# ön plandaki nesnelerin boyutunu küçültmek için aşındırmalar uyguluyoruz
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------------#
#    erosions ->görüntüdeki beyaz bölgeyi küçültür  // dilations -> görüntüdeki beyaz bölgeyi büyütür                #
#--------------------------------------------------------------------------------------------------------------------#

# similarly, dilations can increase the size of the ground objects
# Benzer şekilde, maskede bölgeleri ön plana çıkarabiliriz. 
# Bölgeleri büyütmek için sadece cv2.dilate kullanın
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Masking and bitwise operations
"""
 Maskeler, bir görüntünün ilgilenmediğimiz bölgelerini "maskelememizi" sağlar. 
 "maske" diyoruz çünkü görüntülerin umursamadığımız bölgelerini gizleyeceklerdir.
 Orijinal görüntümüzle karşılaştırıldığında eşikli görüntüyü maske olarak kullanırken,
 görüntünün geri kalanı “maskelendiğinden” renkli bölgeler yeniden görünür
"""
# a typical operation we may want to apply is to take our mask and
# apply a bitwise AND to our input image, keeping only the masked regions
# Uygulamak isteyebileceğimiz tipik bir işlem, 
# maskemizi alıp giriş görselimiz üzerine bit düzeyinde bir "and" işlemi uygulamaktır,
# böylece yalnızca maskelenmiş bölgeleri koruruz.
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)

cv2.waitKey(0)