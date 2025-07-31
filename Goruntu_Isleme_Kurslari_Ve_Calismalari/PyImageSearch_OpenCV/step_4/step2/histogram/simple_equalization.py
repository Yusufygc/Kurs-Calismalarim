"""
Histogram eşitleme, bir görüntünün genel kontrastını artırabilen temel bir görüntü işleme tekniğidir.

Histogram eşitlemeyi uygulamak için, giriş olarak verilen bir gri tonlama/tek-kanallı görüntünün piksel yoğunluklarının histogramını hesaplamakla başlanır:

Dikkat ederseniz, histogramımızda birçok zirve bulunmaktadır, bu da ilgili kovalara birçok pikselin atanmış olduğunu gösterir. Histogram eşitleme ile amacımız, bu pikselleri daha az pikselin atanmış olduğu kovalara dağıtmaktır.


Dikkat ederseniz, giriş görüntüsünün kontrastının önemli ölçüde arttığını fark edersiniz, ancak bunun maliyeti olarak giriş görüntüsündeki gürültünün de kontrastının arttığını görürsünüz.

gürültüyü artırmadan kontrastı artırmak için, adptive histogram eşitleme kullanılabilir.

--- kod kısmı --- adaptive_histogram_equalization
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equalized = clahe.apply(gray)

Notice that we supply two parameters to cv2.createCLAHE:

clipLimit: This is the threshold for contrast limiting
tileGridSize: Divides the input image into M x N tiles and then applies histogram equalization to each local tile

Temel histogram eşitleme, görüntünün genel kontrastını artırmayı amaçlar ve sıkça kullanılan piksel yoğunluklarını "dağıtarak" yapar.
"""

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization
print("[INFO] performing histogram equalization...")
equalized = cv2.equalizeHist(gray)

"""
Note: When performing histogram equalization with OpenCV, we must supply a grayscale/single-channel image. If we try to pass in a multi-channel image, OpenCV will throw an error. To perform histogram equalization on a multi-channel image, you would need to (1) split the image into its respective channels, (2) equalize each channel, and (3) merge the channels back together.

OpenCV ile histogram eşitleme işlemi yaparken, gri tonlamalı/tek kanallı bir görüntü sağlamamız gerekmektedir. Eğer çoklu kanallı bir görüntü geçirmeye çalışırsak, OpenCV bir hata verecektir. Çoklu kanallı bir görüntüde histogram eşitleme yapmak için şu adımları izlemelisiniz: (1) Görüntüyü ilgili kanallarına ayırın, (2) her bir kanalı eşitleyin ve (3) kanalları tekrar birleştirin.
"""

# show the original grayscale image and equalized image
cv2.imshow("Input", gray)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)

















