# import the necessary packages
from transform import four_point_transform
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-c", "--coords",
	help = "comma seperated list of source points")
args = vars(ap.parse_args())

# load the image and grab the source coordinates (i.e. the list of
# (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it.
# Resmi yükleyelim ve kaynak koordinatlarını 
# (örneğin, (x, y) noktaları listesi) alalım.
#  NOTE: 'eval' fonksiyonunu kullanmak kötü bir yöntemdir, 
# ancak bu örnekte şimdilik kabul edelim.
image = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]), dtype = "float32")

# apply the four point tranform to obtain a "birds eye view" of
# the image
# Dört nokta dönüşümünü uygulayarak 
# görüntünün "kuş bakışı" görünümünü elde edelim.
warped = four_point_transform(image, pts)

# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)