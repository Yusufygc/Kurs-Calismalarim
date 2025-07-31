# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to BING objectness saliency model")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-n", "--max-detections", type=int, default=10,
	help="maximum # of detections to examine")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])

# initialize OpenCV's objectness saliency detector and set the path
# to the input model files
saliency = cv2.saliency.ObjectnessBING_create()
saliency.setTrainingPath(args["model"])

# compute the bounding box predictions used to indicate saliency
(success, saliencyMap) = saliency.computeSaliency(image) # saliencyMap: 480x640x1 (1 channel) 
print("[INFO] saliency detection took =" ,saliencyMap)
numDetections = saliencyMap.shape[0] # Mevcut belirginlik tespitlerinin sayısı, döndürülen NumPy dizisinin şekli incelenerek elde edilebilir

# loop over the detections
for i in range(0, min(numDetections, args["max_detections"])):
	# extract the bounding box coordinates
	(startX, startY, endX, endY) = saliencyMap[i].flatten() # flatten(): 1D arraya çevirir (480x640x1 -> 1x307200) 
	
	# randomly generate a color for the object and draw it on the image
	output = image.copy()
	color = np.random.randint(0, 255, size=(3,)) # 0-255 arası 3 tane rastgele sayı üretir (3,): 3 elemanlı dizi oluşturur 
	color = [int(c) for c in color] # 3 elemanlı dizinin elemanlarını int tipine çevirir 
	cv2.rectangle(output, (startX, startY), (endX, endY), color, 2) 
	
	# show the output image
	cv2.imshow("Image", output)
	cv2.waitKey(0)