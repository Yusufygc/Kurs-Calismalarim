# import the necessary packages
import argparse
import imutils
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, type=str,
	help="path to input video file")
ap.add_argument("-o", "--output", required=True, type=str,
	help="path to output directory to store frames")
ap.add_argument("-p", "--min-percent", type=float, default=1.0,
	help="lower boundary of percentage of motion") # Çerçeve hareketi yüzdesinin varsayılan alt sınırı.
ap.add_argument("-m", "--max-percent", type=float, default=10.0,
	help="upper boundary of percentage of motion") # Çerçeve hareketi yüzdesinin varsayılan üst sınırı.
ap.add_argument("-w", "--warmup", type=int, default=200,
	help="# of frames to use to build a reasonable background model") # Makul bir arka plan modeli oluşturmak için kullanılacak çerçevelerin sayısı.
args = vars(ap.parse_args()) 

# initialize the background subtractor
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG() # Çerçeveler arasındaki farkı hesaplamak için kullanılan arka plan çıkarıcıyı başlatır.

# initialize a boolean used to represent whether or not a given frame
# has been captured along with two integer counters -- one to count
# the total number of frames that have been captured and another to
# count the total number of frames processed
captured = False # Verilen bir çerçevenin yakalanıp yakalanmadığını temsil etmek için kullanılan mantıksal değeri başlatır.
total = 0 # Yakalanan toplam çerçeve sayısını saymak için kullanılan bir tamsayıyı başlatır.
frames = 0 # İşlenen toplam çerçeve sayısını saymak için kullanılan bir tamsayıyı başlatır.

# open a pointer to the video file initialize the width and height of
# the frame
vs = cv2.VideoCapture(args["video"]) # Video dosyasına bir işaretçi açar ve çerçevenin genişliğini ve yüksekliğini başlatır.
(W, H) = (None, None) 

# loop over the frames of the video
while True:
	# grab a frame from the video
	(grabbed, frame) = vs.read() # Videodan bir çerçeve yakalar.
	
	# if the frame is None, then we have reached the end of the
	# video file
	if frame is None: # Çerçeve yoksa, video dosyasının sonuna ulaştık demektir.
		break
	
	# clone the original frame (so we can save it later), resize the
	# frame, and then apply the background subtractor
    # Orijinal çerçeveyi kopyalar (daha sonra kaydedebilmemiz için), çerçeveyi yeniden boyutlandırır ve ardından arka plan çıkarıcıyı uygular.
	orig = frame.copy() 
	frame = imutils.resize(frame, width=600)
	mask = fgbg.apply(frame) # Çerçeveler arasındaki farkı hesaplamak için kullanılan arka plan çıkarıcıyı uygular.
	
	# apply a series of erosions and dilations to eliminate noise (morphological operations to eliminate noise.)
	mask = cv2.erode(mask, None, iterations=2) # erode = aşındırma
	mask = cv2.dilate(mask, None, iterations=2) # dilate = genişletme
	
	# if the width and height are empty, grab the spatial dimensions
	if W is None or H is None: # Genişlik ve yükseklik boşsa, mekansal boyutları yakalar.
		(H, W) = mask.shape[:2] # Maske şeklinin ilk iki boyutunu yakalar.
		
	# compute the percentage of the mask that is "foreground"
	p = (cv2.countNonZero(mask) / float(W * H)) * 100 # "ön plan" ve "arka plan" maskelerinin yüzdesini hesaplar. (countNonZero = sıfır olmayan say)  
	
	# if there is less than N% of the frame as "foreground" then we
	# know that the motion has stopped and thus we should grab the
	# frame
	if p < args["min_percent"] and not captured and frames > args["warmup"]: # Eğer çerçevenin N%'den azı "ön plan" ise ve çerçeve yakalanmadıysa ve çerçeve sayısı ısınma süresinden fazlaysa, çerçeveyi yakalar.
		# show the captured frame and update the captured bookkeeping
		# variable
		cv2.imshow("Captured", frame)
		captured = True
		
		# construct the path to the output frame and increment the
		# total frame counter
		filename = "{}.png".format(total)
		path = os.path.sep.join([args["output"], filename])
		total += 1
		
		# save the  *original, high resolution* frame to disk
		print("[INFO] saving {}".format(path))
		cv2.imwrite(path, orig)
		
	# otherwise, either the scene is changing or we're still in warmup
	# mode so let's wait until the scene has settled or we're finished
	# building the background model
	elif captured and p >= args["max_percent"]: # Aksi takdirde, ya sahne değişiyor ya da hala ısınma modundayız, bu yüzden sahne yerleşene kadar veya arka plan modelini oluşturmayı bitirene kadar bekleyelim.
		captured = False # Yakalanan çerçeve yok.
		
        
    # Özetlemek gerekirse, tüm karelerin işlenmesi bitene kadar çerçeveyi ve maskeyi görüntüleyeceğiz
	
    # display the frame and detect if there is a key press
	cv2.imshow("Frame", frame)
	cv2.imshow("Mask", mask)
	key = cv2.waitKey(1) & 0xFF
	
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	
	# increment the frames counter
	frames += 1
	
# do a bit of cleanup
vs.release()



