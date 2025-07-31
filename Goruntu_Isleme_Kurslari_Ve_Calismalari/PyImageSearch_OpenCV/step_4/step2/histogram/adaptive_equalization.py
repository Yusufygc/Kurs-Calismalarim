# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to the input image")
ap.add_argument("-c", "--clip", type=float, default=2.0,
	help="threshold for contrast limiting")
ap.add_argument("-t", "--tile", type=int, default=8,
	help="tile grid size -- divides image into tile x time cells")
args = vars(ap.parse_args())

#-----------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------#
"""
Sonra üç komut satırı argümanımız var, bunlardan biri zorunlu, diğer ikisi ise isteğe bağlıdır (ancak CLAHE ile deney yaparken ayarlama ve oynamak için kullanışlıdır):

--image: Histogram eşitleme uygulamak istediğimiz giriş görüntünün diskteki yolunu belirtir.

--clip: Kontrast sınırlama için eşik değeri. Genellikle bu değeri 2-5 aralığında tutmak istersiniz. Eğer değeri çok büyük ayarlarsanız, etkin olarak yerel kontrastı en üst düzeye çıkarırsınız ve bu da gürültüyü maksimum seviyeye çıkarır (bu istediğinizin tam tersidir). Bunun yerine, bu değeri mümkün olduğunca düşük tutmaya çalışın.

--tile: CLAHE için kare yaprağı büyüklüğü. Kavramsal olarak, burada yapmaya çalıştığımız, giriş görüntümüzü yaprak x yaprak hücrelere bölmek ve ardından her hücreye histogram eşitlemesi uygulamaktır (CLAHE'nin sağladığı ek özelliklerle birlikte).

Şimdi OpenCV ile CLAHE uygulayalım:
"""
#-----------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------#
"""
Geleneksel bir yöntem olarak “Adaptive Histogram Equalization” kullanırız ancak bu durumda global contrass değerini kullanmak zorundayiz. Bunu sonucu olarak görüntüde farklı bölgelerde çok karanlık ve çok patlamış bölgeler oluşabilir. Bu sorunu çözebilmek adına alternatif bir yöntem olan CLAHE (Contrast Limited Adaptive Histogram Equazation) kullanabiliriz.

CLAHE yönteminin geleneksel equalization’a göre farkı, görüntüyü 8x8 gibi parçalara ayırarak her bir kare içerisinde histogram equalization yapmasıdır, ayrıca contrass limiti belirleme imkanı tanınır. Böylece daha temiz istediğimiz bilgilerin ayrıştığı bir görüntü elde edebililiriz.
"""
#-----------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------#
# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
print("[INFO] applying CLAHE...")
clahe = cv2.createCLAHE(clipLimit=args["clip"],
	tileGridSize=(args["tile"], args["tile"]))
equalized = clahe.apply(gray)

# show the original grayscale image and CLAHE output image
cv2.imshow("Input", gray)
cv2.imshow("CLAHE", equalized)
cv2.waitKey(0)

"""
Kendi görüntü işleme akışınızı oluştururken ve histogram eşitlemenin uygulanması gerektiğini düşündüğünüzde, önerim cv2.equalizeHist kullanarak basit histogram eşitleme ile başlamanızdır. Ancak sonuçların kötü olduğunu ve giriş görüntüsündeki gürültüyü artırdığınızı fark ederseniz, cv2.createCLAHE kullanarak adaptif histogram eşitlemeyi denemenizdir.
"""