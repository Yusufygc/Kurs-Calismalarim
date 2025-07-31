# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output video file")
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
ap.add_argument("-f", "--fps", type=int, default=60,
	help="FPS of output video") 
ap.add_argument("-c", "--codec", type=str, default="MJPG", # MJPG, XVID, X264, WMV1, WMV2 
	help="codec of output video")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera
# sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start() # VideoStream
time.sleep(2.0)

# initialize the FourCC, video writer, dimensions of the frame, and
# zeros array
fourcc = cv2.VideoWriter_fourcc(*args["codec"]) # MJPG, XVID, X264, WMV1, WMV2 
writer = None # cv2.VideoWriter
(h, w) = (None, None) # frame dimensions
zeros = None # np.zeros

# loop over frames from the video stream
while True:
	# grab the frame from the video stream and resize it to have a
	# maximum width of 300 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=300)
	frame = cv2.flip(frame, 1) # ayna efekti 0 dikey 1 yatay 2 hem dikey hem yatay
	
    # check if the writer is None
	if writer is None:
		# store the image dimensions, initialize the video writer, 
		# and construct the zeros array 
		(h, w) = frame.shape[:2] 
		writer = cv2.VideoWriter(args["output"], fourcc, args["fps"],
			(w * 2, h * 2), True) 
		zeros = np.zeros((h, w), dtype="uint8") 
		#-----------------------------------------------------------------------------------------------------------------------------
		"""
        The cv2.VideoWriter requires five parameters:

        The first parameter is the path to the output video file. In this case, we’ll supply the value of the --output switch, which is the path to where our video file will live on disk.
	
        Secondly, we need to supply the fourcc codec.
	
        The third argument to cv2.VideoWriter is the desired FPS of the output video file.
	
        We then have the width and height of output video. It’s important that you set these values correctly, otherwise OpenCV will throw an error if you try to write a frame to file that has different dimensions than the ones supplied to cv2.VideoWriter .
	
        Finally, the last parameter controls whether or not we are writing color frames to file. A value of True indicates that we are writing color frames. Supplying False indicates we are not writing color frames.
        #-----------------------------------------------------------------------------------------------------------------------------
        cv2.VideoWriter beş parametre gerektirir: İlk parametre, çıktı video dosyasının yoludur. Bu durumda, video dosyamızın diskte yaşayacağı yol olan --output anahtarının değerini sağlayacağız. 
	
	    İkinci olarak, fourcc codec'i sağlamamız gerekiyor. 
	    
	    cv2.VideoWriter'ın üçüncü argümanı, çıktı video dosyasının istenen FPS değeridir. Daha sonra çıktı videosunun genişliğine ve yüksekliğine sahibiz. Bu değerleri doğru ayarlamanız önemlidir, aksi takdirde cv2.VideoWriter için sağlananlardan farklı boyutlara sahip bir çerçeveyi dosyaya yazmaya çalışırsanız OpenCV hata verir. 
	    
	    Son olarak, son parametre dosyaya renkli çerçeveler yazıp yazmadığımızı kontrol eder. True değeri, renkli çerçeveler yazdığımızı gösterir. False değerini belirtmek, renkli çerçeveler yazmadığımızı gösterir.
        """
		#-----------------------------------------------------------------------------------------------------------------------------
		
    # break the image into its RGB components, then construct the
	# RGB representation of each frame individually
	(B, G, R) = cv2.split(frame) # renk kanallarını böldük
	R = cv2.merge([zeros, zeros, R]) # sadece kırımızı kanalı gösteren bir görüntü oluşturduk 
	G = cv2.merge([zeros, G, zeros]) # sadece yeşil kanalı gösteren bir görüntü oluşturduk
	B = cv2.merge([B, zeros, zeros]) # sadece mavi kanalı gösteren bir görüntü oluşturduk 
	# sıfırları kullanarak her kanalın bir temsilini oluştururuz
	
    # construct the final output frame, storing the original frame
	# at the top-left, the red channel in the top-right, the green
	# channel in the bottom-right, and the blue channel in the
	# bottom-left 
    # orijinal çerçeveyi sol üstte, 
    # kırmızı kanalı sağ üstte, 
    # yeşil kanalı sağ altta ve
    #  mavi kanalı sol altta saklayarak nihai çıktı çerçevesini oluşturalım.
	output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
	output[0:h, 0:w] = frame # orijinal çerçeveyi sol üstte saklayalım
	output[0:h, w:w * 2] = R # kırmızı kanalı sağ üstte saklayalım
	output[h:h * 2, w:w * 2] = G # yeşil kanalı sağ altta saklayalım
	output[h:h * 2, 0:w] = B # mavi kanalı sol altta saklayalım
	# write the output frame to file
	writer.write(output)
	
    # show the frames
	cv2.imshow("Frame", frame)
	cv2.imshow("Output", output)
	key = cv2.waitKey(1) & 0xFF
	
    # if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	
# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows() 
vs.stop() 
writer.release() # video dosyasını serbest bırakalım