## Barkod içeren bir video oluşturunuz ya da bulunuz benim kullandığım video doğru dürüst çalışmadı
# import the necessary packages
import simple_barcode_detection
from imutils.video import VideoStream
import argparse
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())

# if the video path was not supplied, grab the reference to the
# camera
if not args.get("video", False): # eğer video yolu verilmediyse
	vs = VideoStream(src=0).start() # kameradan görüntü al
	time.sleep(2.0) # 2 saniye bekle

# otherwise, load the video
else: # eğer video yolu verildiyse
	vs = cv2.VideoCapture(args["video"]) # videoyu yükle
	
# keep looping over the frames
while True:
	# grab the current frame and then handle if the frame is returned
	# from either the 'VideoCapture' or 'VideoStream' object,
	# respectively
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame # eğer video yolu verildiyse frame[1] değilse frame alıyoruz (VideoStream veya cv2.VideoCapture kullanıp kullanmadığımızı ele alıyoruz.)
 
	# check to see if we have reached the end of the
	# video
	if frame is None:
		break
	
	# detect the barcode in the image
	box = simple_barcode_detection.detect(frame) # frame'de barkod var mı diye bakıyoruz (simple_barcode_detection.py'deki detect fonksiyonunu kullanıyoruz) 
	
	# if a barcode was found, draw a bounding box on the frame
	if box is not None:
		cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
		
	# show the frame and record if the user presses a key
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	
# if we are not using a video file, stop the video file stream
# aşağıdaki satırlar video akış nesnemizi temizleme işaretçileridir. Eğer video yolu verilmediyse, kameradan görüntü alıyorduk. Bu yüzden VideoStream nesnesini durduruyoruz. Eğer video yolu verildiyse, VideoCapture nesnesini serbest bırakıyoruz.
if not args.get("video", False): 
	vs.stop()
	
# otherwise, release the camera pointer
else:
	vs.release()
	
# close all windows
cv2.destroyAllWindows()