# import the necessary packages
from pyimagesearch.keyclipwriter import KeyClipWriter
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output directory")
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
ap.add_argument("-f", "--fps", type=int, default=20,
	help="FPS of output video")
ap.add_argument("-c", "--codec", type=str, default="MJPG",
	help="codec of output video")
ap.add_argument("-b", "--buffer-size", type=int, default=32, # buffer-size: önbellek boyutu
	help="buffer size of video clip writer")
args = vars(ap.parse_args())

"""
Kamera sensöründen en son sorgulanan kareleri depolamak 
için kullanılan bellek içi arabelleğin boyutu. 
Daha büyük bir --buffer-size, çıkış video klibinde "temel olaydan" 
önce ve sonra daha fazla bağlamın dahil edilmesine izin verirken, 
daha küçük bir --buffer-size, "temel olaydan" önce ve sonra daha az kare depolar.
"""

# initialize the video stream and allow the camera sensor to
# warmup
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# define the lower and upper boundaries of the "green" ball in
# the HSV color space
greenLower = (29, 86, 6) # HSV renk uzayında "yeşil" topun alt ve üst sınırlarını tanımlayın
greenUpper = (64, 255, 255) 

# initialize key clip writer and the consecutive number of
# frames that have *not* contained any action
kcw = KeyClipWriter(bufSize=args["buffer_size"]) 
consecFrames = 0
"""
satrı 45 herhangi bir ilginç olay içermeyen ardışık çerçevelerin sayısını 
saymak için kullanılan bir tamsayıyı başlatmanın yanı sıra,
sağladığımız --buffer-size'yi kullanarak KeyClipWriter'ımızı başlatır.
"""

# keep looping
while True:
	# grab the current frame, resize it, and initialize a
	# boolean used to indicate if the consecutive frames
	# counter should be updated
	frame = vs.read()
	frame = imutils.resize(frame, width=600)
	updateConsecFrames = True

	# blur the frame and convert it to the HSV color space
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper) # Bu yöntem, greenLower <= p <= greenUpper olan tüm p piksellerini bulur.
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2) 
	# Ardından, maskede kalan küçük lekeleri çıkarmak 
    # için bir dizi aşındırma ve genişleme gerçekleştiriyoruz.(erode ve dilate)
	
	# find contours in the mask
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	
    # only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use it
		# to compute the minimum enclosing circle
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		updateConsecFrames = radius <= 10
		
		"""Satır 81, en az bir konturun bulunduğundan emin olmak 
	    için bir kontrol yapar ve öyleyse, Satır 84 ve 86 maskedeki 
	    (alana göre) en büyük konturu bulur ve bu konturu minimum 
	    çevreleyen daireyi hesaplamak için kullanır."""
		
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# reset the number of consecutive frames with
			# *no* action to zero and draw the circle
			# surrounding the object
			consecFrames = 0
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 0, 255), 2)
			"""
	        Dairenin yarıçapı minimum 10 piksel boyutunu karşılıyorsa 
	        (Satır 94), o zaman yeşil topu bulduğumuzu varsayacağız.
	        98-100 satırları, herhangi bir ilginç olay içermeyen 
	        consecFrame'lerin sayısını sıfırlar (çünkü ilginç bir olay "şu anda oluyor")
	        ve çerçevede topumuzu vurgulayan bir daire çizelim.
	        """
			# if we are not already recording, start recording
			if not kcw.recording:
				timestamp = datetime.datetime.now()
				p = "{}/{}.avi".format(args["output"],
					timestamp.strftime("%Y%m%d-%H%M%S"))
				kcw.start(p, cv2.VideoWriter_fourcc(*args["codec"]),
					args["fps"])
				"""
		        Son olarak, şu anda bir video klip kaydedip kaydetmediğimizi
		        kontrol ediyoruz (Satır 83). Değilse, geçerli zaman damgasına
		        dayalı olarak video klip için bir çıktı dosya adı
		        oluştururuz ve KeyClipWriter'ın başlatma yöntemini çağırırız. 
		        Bu yöntem, video klip kaydını başlatır ve ardından video klip yazıcısını başlatır.
		    """
				
            # Otherwise, we’ll assume no key/interesting event has taken place:

	# otherwise, no action has taken place in this frame, so
	# increment the number of consecutive frames that contain
	# no action
	if updateConsecFrames: 
		# aksi takdirde, bu çerçevede hiçbir eylem gerçekleşmediğinden, 
		# eylem içermeyen ardışık çerçevelerin sayısını artıralım
		consecFrames += 1
		
	# update the key frame clip buffer
	kcw.update(frame) # anahtar çerçeve klibi arabelleğini güncelleyelim
	
	# if we are recording and reached a threshold on consecutive
	# number of frames with no action, stop recording the clip
	if kcw.recording and consecFrames == args["buffer_size"]:
		kcw.finish() 
		# kayıt yapıyorsak ve ardışık çerçevelerin sayısı 
		# eylem içermiyorsa, klibi kaydetmeyi bırakalım

	
    # show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	
    # if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break            
	

# if we are in the middle of recording a clip, wrap it up
if kcw.recording:
	kcw.finish()
	
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()