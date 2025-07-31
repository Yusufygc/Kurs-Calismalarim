#--------------------------------------------------------------------------------------------------------------------#
# cmd python rotate_pills.py --image images/pill_01.png                                                                   #
#--------------------------------------------------------------------------------------------------------------------#
# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# load the image from disk, convert it to grayscale, blur it,
# and apply edge detection to reveal the outline of the pill
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 20, 100) 
# Canny kenar algılama algoritması, görüntüdeki kenarları algılamak için kullanılan bir görüntü işleme yöntemidir.

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


# We are now ready to extract the pill ROI from the image:

# ensure at least one contour was found // en az bir kontur bulunduğundan emin olun
if len(cnts) > 0:
	# grab the largest contour, then draw a mask for the pill
	# en büyük konturu alalım, ardından hap için bir maske çizelim.
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)

	# compute its bounding box of pill, then extract the ROI,
	# and apply the mask
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = image[y:y + h, x:x + w] 
	# Hem sınırlayıcı kutuyu hem de maskeyi kullanarak 
	# gerçek hap bölgesi ROI'sini (Satır 42-45) çıkarabiliriz.
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,
		mask=maskROI)

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

	# loop over the rotation angles
	# döndürme açıları üzerinde döngü kuralım.
	for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate(imageROI, angle)
		cv2.imshow("Rotated (Problematic)", rotated)
		cv2.waitKey(0)
		
	# loop over the rotation angles again, this time ensure the
	# entire pill is still within the ROI after rotation
	# dönüş açıları üzerinden tekrar döngü yapalım,
	# bu sefer tüm hapın dönüşten sonra hala ROI içinde olduğundan emin olalım
	for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate_bound(imageROI, angle)
		cv2.imshow("Rotated (Correct)", rotated)
		cv2.waitKey(0)

"""
rotate_bound fonksiyonu, OpenCV'de döndürme işlevselliğini uygulamak için kullanılan bir işlevdir.ve aşağıdaki işlmeleri yapar:

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))
    
"""