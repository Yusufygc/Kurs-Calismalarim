# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"]) # resmi okuruz

# initialize OpenCV's static saliency spectral residual detector and
# compute the saliency map
saliency = cv2.saliency.StaticSaliencySpectralResidual_create() # saliency nesnesi oluştururuz
(success, saliencyMap) = saliency.computeSaliency(image) # saliency haritasını hesaplaruz  
saliencyMap = (saliencyMap * 255).astype("uint8") # saliency haritasını 0-255 arasına çekeriz
cv2.imshow("Image", image)
cv2.imshow("Output", saliencyMap)
cv2.waitKey(0)

"""
Sonuç, görüntünün en belirgin, göze çarpan bölgelerini vurgulayan kayan noktalı, 
gri tonlamalı bir görüntü olan saliencyMap'tir. Kayan nokta değerlerinin aralığı [0, 1] 
olup, 1'e yakın değerler "ilginç" alanları, 0'a yakın değerler ise "ilginç olmayan"
alanları temsil eder.
"""

# initialize OpenCV's static fine grained saliency detector and
# compute the saliency map
saliency = cv2.saliency.StaticSaliencyFineGrained_create() 
(success, saliencyMap) = saliency.computeSaliency(image) 

# if we would like a *binary* map that we could process for contours,
# compute convex hull's, extract bounding boxes, etc., we can
# additionally threshold the saliency map
threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # saliency haritasını binary hale getiririz 

# show the images
cv2.imshow("Image", image)
cv2.imshow("Output", saliencyMap)
cv2.imshow("Thresh", threshMap)
cv2.waitKey(0)