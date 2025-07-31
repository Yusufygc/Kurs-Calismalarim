# import the necessary packages
from skimage import transform
from skimage import filters
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image file")
ap.add_argument("-d", "--direction", type=str,
	default="vertical", help="seam removal direction")
args = vars(ap.parse_args())
"""
Dikiş oyma işlemini uygulayacağımız yön. Dikey değeri görüntü genişliğini 
ayarlarken yatay değeri görüntünün yüksekliğini ayarlar. 
Oyma yönünü varsayılan olarak dikey olarak ayarladık.
"""

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute the Sobel gradient magnitude representation
# of the image -- this will serve as our "energy map"
# input to the seam carving algorithm
mag = filters.sobel(gray.astype("float")) # Sobel gradyan büyüklüğünü hesaplar. Bu, oyma algoritmasına giriş olarak hizmet edecektir. # gray.astype("float"): gri görüntüyü ondalık sayıya dönüştürür. # filters.sobel: Sobel gradyan büyüklüğünü hesaplayan fonksiyon # mag: görüntünün kenarlık haritası (enerji haritası) 

# show the original image
cv2.imshow("Original", image)

# loop over a number of seams to remove
for numSeams in range(20, 140, 20):
	# perform seam carving, removing the desired number
	# of frames from the image -- `vertical` cuts will
	# change the image width while `horizontal` cuts will
	# change the image height
	carved = transform.seam_carve(image, mag, args["direction"],
		numSeams) # numSeams: oyma işleminden kaldırılacak dikiş sayısı  # args["direction"]: oyma yönü (dikey veya yatay) # mag: görüntünün kenarlık haritası (enerji haritası) # image: giriş görüntüsü # carved: oyma işleminden sonra görüntü # transform.seam_carve: oyma işlemini gerçekleştiren fonksiyon
	print("[INFO] removing {} seams; new size: "
		"w={}, h={}".format(numSeams, carved.shape[1],
			carved.shape[0]))
	
	# show the output of the seam carving algorithm
	cv2.imshow("Carved", carved)
	cv2.waitKey(0)

	"""
	AttributeError: module 'skimage.transform' has no attribute 'seam_carve' hatası verdi
	"""