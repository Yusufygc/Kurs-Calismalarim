import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
# bağımsız değişkenleri oluşturuyoruz ve bağımsız değişkenleri ayrıştırıyoruz
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-o", "--output", required=True,
	help="path to output image")
args = vars(ap.parse_args())

# load the input image from disk
# resmi diskten yüklüyoruz
image = cv2.imread(args["input"])

# convert the image to grayscale, blur it, and threshold it
# resmi griye çeviriyoruz, bulanıklaştırıyoruz ve eşik değerini belirliyoruz 
# bu işlemleri yapmamızın sebebi resimdeki şekilleri daha iyi ayırt edebilmek
# ve işlem hızını arttırmak
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

######################################################################################

# extract contours from the image
# resimden konturları çıkarıyoruz (kontur: resimdeki şekillerin dış hatları)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
cnts = imutils.grab_contours(cnts)

# loop over the contours and draw them on the input image
# konturlar üzerinde döngü oluşturuyoruz ve girdi resminin üzerine çiziyoruz
for c in cnts:
	cv2.drawContours(image, [c], -1, (0, 0, 255), 2)

# display the total number of shapes on the image
# resimdeki toplam şekil sayısını resmin köşesine yazdırıyoruz
text = "I found {} total shapes".format(len(cnts))
cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
		(0, 0, 255), 2)

# write the output image to disk
# çıktı resmini diske yazdırıyoruz
cv2.imwrite(args["output"], image)









