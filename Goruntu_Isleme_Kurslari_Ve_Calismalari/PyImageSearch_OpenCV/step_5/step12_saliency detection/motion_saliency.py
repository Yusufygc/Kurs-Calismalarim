# import the necessary packages
from imutils.video import VideoStream
import imutils
import time
import cv2

# initialize the motion saliency object and start the video stream
saliency = None
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to 500px (to speedup processing)
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	frame = cv2.flip(frame,1)
	
	# if our saliency object is None, we need to instantiate it
	if saliency is None: 
		saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create() # MotionSaliencyBinWangApr2014_create(): MotionSaliencyBinWangApr2014 sınıfının bir örneğini oluşturur
		saliency.setImagesize(frame.shape[1], frame.shape[0]) # setImagesize(width, height)
		saliency.init() # init(): MotionSaliencyBinWangApr2014 sınıfının örneğini başlatır
		
	# convert the input frame to grayscale and compute the saliency
	# map based on the motion model
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	(success, saliencyMap) = saliency.computeSaliency(gray) # computeSaliency(image): Giriş görüntüsüne göre hareket modeline dayalı olarak görünürlük haritasını hesaplar. Wang yöntemi gri tonlamalı çerçeveler gerektirir.
	saliencyMap = (saliencyMap * 255).astype("uint8") # saliencyMap * 255: 0-1 arasındaki değerleri 0-255 arasına çevirir
	# astype("uint8"): 0-255 arasındaki değerleri 0-255 arasına çevirir
	# display the image to our screen
	cv2.imshow("Frame", frame)
	cv2.imshow("Map", saliencyMap)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()