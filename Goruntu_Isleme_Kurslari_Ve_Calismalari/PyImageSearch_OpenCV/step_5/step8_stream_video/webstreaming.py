# import the necessary packages
from pyimsgesearch.motion_detection.singlemotiondetector import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response # Response sınıfı, bir HTTP yanıtı oluşturmak için kullanılır.
from flask import Flask # Flask sınıfı, bir WSGI uygulaması oluşturmak için kullanılır. WSGI (Web Server Gateway Interface), Python uygulamalarının web sunucularıyla iletişim kurmasını sağlayan bir standarttır.
from flask import render_template # render_template fonksiyonu, bir Jinja2 şablonunu kullanarak HTML sayfaları oluşturmak için kullanılır. Jinja2, Python için tam özellikli bir şablon motorudur. 
import threading # threading modülü, birden fazla iş parçacığı oluşturmak için kullanılır.
import argparse # argparse modülü, komut satırı argümanlarını analiz etmek için kullanılır.
import datetime # datetime modülü, tarih ve saat bilgilerini işlemek için kullanılır.
import imutils # imutils modülü, OpenCV işlevlerini kolaylaştırmak için kullanılır.
import time # time modülü, zamanla ilgili işlemler yapmak için kullanılır.
import cv2 

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None # outputFrame, görüntü akışı için çıktı çerçevesini tutar.
lock = threading.Lock() # lock, çıktı çerçevelerinin güvenli bir şekilde değiştirilmesini sağlamak için kullanılır. oututFrame'i güncellerken iş parçacığı güvenli davranışı sağlamak için kullanılacak bir kilit oluşturuyoruz (yani, bir iş parçacığının güncellenirken çerçeveyi okumaya çalışmadığından emin oluyoruz).

# initialize a flask object
app = Flask(__name__) # app, Flask uygulamasını başlatır.

# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)

@app.route("/") # /, uygulamanın kök dizinini temsil eder. 
def index(): 
	# return the rendered template
	return render_template("index.html") # index.html dosyasını döndürür.
    # Bu işlev oldukça basittir — tek yaptığı HTML dosyamızda Flask render_template'i çağırmak

def detect_motion(frameCount): # detect_motion fonksiyonu, hareket algılama işlemini gerçekleştirir. ftrameCount, kaç çerçeve boyunca hareket algılanacağını belirtir.
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, outputFrame, lock # vs, outputFrame ve lock değişkenlerini global olarak tanımlıyoruz.
	"""
	vs: Örneklenmiş VideoStream nesnemiz
	outputFrame: İstemcilere sunulacak çıktı
	lock : outputFrame'i güncellemeden önce elde etmemiz gereken iş parçacığı kilidi
	"""
	# initialize the motion detector and the total number of frames
	# read thus far
	md = SingleMotionDetector(accumWeight=0.1) # SingleMotionDetector sınıfını md olarak tanımlıyoruz.
	"""
	SingleMotionDetector sınıfımızı bir accumWeight=0,1 değeriyle başlatır; bu, ağırlıklı ortalama hesaplanırken bg değerinin daha yüksek ağırlıklı olacağını ima eder.
	"""
	total = 0 # total, şu ana kadar okunan toplam çerçeve sayısını tutar.
	"""
	En az frameCount karemiz yoksa, birikmiş ağırlıklı ortalamayı hesaplamaya devam edeceğiz
	frameCount'a ulaşıldığında, arka plan çıkarma işlemini gerçekleştirmeye başlayacağız.
	"""

	# loop over frames from the video stream
	while True:
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (7, 7), 0)

		# grab the current timestamp and draw it on the frame
		timestamp = datetime.datetime.now() # timestamp, şu anki zaman damgasını tutar.
		cv2.putText(frame, timestamp.strftime(
			"%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1) # strftime, tarih ve saat bilgilerini biçimlendirmek için kullanılır. strftime, datetime nesnesinin bir yöntemidir.
		

		# if the total number of frames has reached a sufficient
		# number to construct a reasonable background model, then
		# continue to process the frame
		if total > frameCount: # total, frameCount'a ulaştığında, arka plan çıkarma işlemini gerçekleştirmeye başlayacağız.
			# detect motion in the image
			motion = md.detect(gray) # md.detect, gri tonlamalı görüntüdeki hareketi algılar.

			# check to see if motion was found in the frame
			if motion is not None: # motion, boş değilse, hareket algılanmıştır.
				# unpack the tuple and draw the box surrounding the
				# "motion area" on the output frame
				(thresh, (minX, minY, maxX, maxY)) = motion 
				cv2.rectangle(frame, (minX, minY), (maxX, maxY),
					(0, 0, 255), 2) 
		
		# update the background model and increment the total number
		# of frames read thus far
		md.update(gray) # md.update, arka plan modelini günceller.
		total += 1 

		# acquire the lock, set the output frame, and release the
		# lock
		with lock:
			 # lock, çıktı çerçevelerinin güvenli bir şekilde değiştirilmesini sağlamak için kullanılır. oututFrame'i güncellerken iş parçacığı güvenli davranışı sağlamak için kullanılacak bir kilit oluşturuyoruz (yani, bir iş parçacığının güncellenirken çerçeveyi okumaya çalışmadığından emin oluyoruz).
			outputFrame = frame.copy() 

def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock

	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop

			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame) # cv2.imencode, görüntüyü belirtilen biçimde kodlar. .jpg, JPEG biçimini belirtir. outputFrame, görüntü akışı için çıktı çerçevesini tutar. 

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed") # /video_feed, video akışını temsil eder. app.route, uygulamaya bir URL kuralı ekler. 
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(), 
		mimetype = "multipart/x-mixed-replace; boundary=frame") # Response, bir HTTP yanıtı oluşturmak için kullanılır. generate(), görüntü akışını oluşturur. mimetype, içerik türünü belirtir. multipart/x-mixed-replace, birden fazla içeriğin tek bir yanıtta gönderilmesini sağlar. boundary, içerikler arasında ayırıcı olarak kullanılan dizeyi belirtir.
"""
app.route imzası, Flask'a bu işlevin bir URL uç noktası 
olduğunu ve verilerin http://ip_adresiniz/video_feed adresinden sunulduğunu bildirir.
"""
# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	args = vars(ap.parse_args())

	# start a thread that will perform motion detection
	t = threading.Thread(target=detect_motion, args=(
		args["frame_count"],)) 
	t.daemon = True
	t.start()

	# start the flask app
	app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
	
# release the video stream pointer
vs.stop()