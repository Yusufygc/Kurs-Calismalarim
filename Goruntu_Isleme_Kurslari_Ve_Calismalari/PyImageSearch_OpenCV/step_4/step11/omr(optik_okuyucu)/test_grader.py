"""
Step #1: Detect the exam in an image.
Step #2: Apply a perspective transform to extract 
		 the top-down, birds-eye-view of the exam.
Step #3: Extract the set of bubbles (i.e., the possible answer choices)
		 from the perspective transformed exam.
Step #4: Sort the questions/bubbles into rows.
Step #5: Determine the marked (i.e., “bubbled in”) answer for each row.
Step #6: Lookup the correct answer in our answer key 
		 to determine if the user was correct in their choice.
Step #7: Repeat for all questions in the exam.

https://pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/
"""

# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# define the answer key which maps the question number
# to the correct answer
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1} 
# (0: A, 1: B, 2: C, 3: D, 4: E bunu copilot yazdırdı ama hayırlısı)
# Değişkenin adından da anlaşılacağı gibi, ANSWER_KEY 
# soru numaralarının tamsayı eşlemelerini doğru balonun dizinine sağlar.
"""
Bu durumda, 0 anahtarı ilk soruyu gösterirken, 
1 değeri doğru cevap olarak “B”yi gösterir 
(“B”, “ABCDE” dizgisindeki 1 indeksidir). 
İkinci bir örnek olarak, 4 değerine karşılık gelen 1 anahtarını ele alalım 
— bu, ikinci sorunun cevabının "E" olduğunu gösterir.
"""

# load the image, convert it to grayscale, blur it
# slightly, then find edges
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)


cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)


# find contours in the edge map, then initialize
# the contour that corresponds to the document 
# (correspond = eşleşmek,karşılık gelmek)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None

# ensure that at least one contour was found
# en az bir kontur bulunduğundan emin olun
if len(cnts) > 0:
	# sort the contours according to their size in
	# descending order 
	# Kenarları büyüklüklerine göre azalan sırayla sıralayalım.
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
	
	# loop over the sorted contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		
		# if our approximated contour has four points,
		# then we can assume we have found the paper
		if len(approx) == 4:
			docCnt = approx
			break
"""
Bunu, Hat 71'de (tabii ki Satır 67'te en az bir kontur bulunduğundan emin olduktan sonra)
konturlarımızı alanlarına göre (büyükten küçüğe) sıralayarak yapıyoruz. 
Bu, daha büyük konturların listenin önüne yerleştirileceği, 
daha küçük konturların ise listenin daha gerisinde görüneceği anlamına gelir.
"""

# apply a four point perspective transform to both the
# original image and grayscale image to obtain a top-down
# birds eye view of the paper
paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))
"""
Konturlarımızın (x, y)-koordinatlarını belirli, 
tekrarlanabilir bir şekilde düzenler. 
Bölgeye bir perspektif dönüşümü uygular
"""

# apply Otsu's thresholding method to binarize the warped
# piece of paper 
thresh = cv2.threshold(warped, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# find contours in the thresholded image, then initialize
# the list of contours that correspond to questions
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour, then use the
	# bounding box to derive the aspect ratio 
	# (derive = türetmek,-den elde etmek)
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)
	
    # in order to label the contour as a question, region
	# should be sufficiently wide, sufficiently tall, and
	# have an aspect ratio approximately equal to 1
	# Bir kenarı soru olarak etiketlemek için,
	# bölgenin yeterince geniş, yeterince uzun olması
	# ve en-boy oranının yaklaşık olarak 
	# 1'e eşit olması gerekmektedir.
	if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
		questionCnts.append(c)
		
# sort the question contours top-to-bottom, then initialize
# the total number of correct answers
# soru konturlarını yukarıdan aşağıya sıralayalım,
# ardından toplam doğru cevap sayısını sıfırlayalım.
questionCnts = contours.sort_contours(questionCnts,
	method="top-to-bottom")[0]
correct = 0

# each question has 5 possible answers, to loop over the
# question in batches of 5
# her sorunun 5 olası cevabı vardır, 
# soru için 5'lik gruplar halinde döngü oluşturalım.
for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
	# sort the contours for the current question from
	# left to right, then initialize the index of the
	# bubbled answer
	# mevcut soru için konturları soldan sağa sıralayalım,
	# ardından kabarcıklı cevabın dizinini başlatalım.
	cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
	bubbled = None
	
# loop over the sorted contours
	for (j, c) in enumerate(cnts):
		# construct a mask that reveals only the current
		# "bubble" for the question
		# soru için yalnızca mevcut "baloncuk" u 
		# ortaya çıkaran bir maske oluşturalım.
		mask = np.zeros(thresh.shape, dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)
		
		# apply the mask to the thresholded image, then
		# count the number of non-zero pixels in the
		# bubble area
		# maskeyi eşiklenmiş görüntüye uygulayalım,
		# ardından kabarcık alanındaki sıfır olmayan piksellerin
		# sayısını sayalım.
		mask = cv2.bitwise_and(thresh, thresh, mask=mask)
		total = cv2.countNonZero(mask)
		
		# if the current total has a larger number of total
		# non-zero pixels, then we are examining the currently
		# bubbled-in answer
		# Eğer mevcut toplamda 
		# daha fazla sayıda toplamı sıfır olmayan piksel varsa, 
		# o zaman şu anda işaretlenmiş olan cevabı inceliyoruz demektir.
		if bubbled is None or total > bubbled[0]:
			bubbled = (total, j)
			
    # initialize the contour color and the index of the
	# *correct* answer
	color = (0, 0, 255)
	k = ANSWER_KEY[q]
	
	# check to see if the bubbled answer is correct
	if k == bubbled[1]:
		color = (0, 255, 0)
		correct += 1
		
	# draw the outline of the correct answer on the test
	cv2.drawContours(paper, [cnts[k]], -1, color, 3)    
	
# grab the test taker
# sınavı alan kişiyi tutalım ve sınav sonucunu gösterelim.:)
score = (correct / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper, "{:.2f}%".format(score), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", paper)
cv2.waitKey(0)