# import the necessary packages
from collections import deque # deque: double-ended queue
from threading import Thread # Thread: a thread of execution in a program
from queue import Queue # Queue: a FIFO queue 
import time # time: time-related functions
import cv2 

class KeyClipWriter:
	def __init__(self, bufSize=64, timeout=1.0):
		# store the maximum buffer size of frames to be kept
		# in memory along with the sleep timeout during threading
		self.bufSize = bufSize
		self.timeout = timeout
       
		"""
	    bufSize : The maximum number of frames to be keep cached in an in-memory buffer.
        timeout : An integer representing the number of seconds to sleep for 
	    when (1) writing video clips to file and (2) there are no frames ready to be written.
	    
	    bufSize : Bellek içi arabellekte önbelleğe alınacak maksimum çerçeve sayısı. 
	    timeout : (1) video klipleri dosyaya yazarken ve (2) yazılmaya hazır çerçeve 
	    olmadığında uykuya geçilecek saniye sayısını temsil eden bir tamsayı.
        """

		# initialize the buffer of frames, queue of frames that
		# need to be written to file, video writer, writer thread,
		# and boolean indicating whether recording has started or not
		self.frames = deque(maxlen=bufSize)
		self.Q = None
		self.writer = None
		self.thread = None
		self.recording = False

		"""
		frames : A buffer used to a store a maximum of bufSize frames 
				that have been most recently read from the video stream.
		Q : A “first in, first out” (FIFO) Python Queue data structure 
			used to hold frames that are awaiting to be written to video file.
		writer : An instantiation of the cv2.VideoWriter class 
				used to actually write frames to the output video file.
		thread : A Python Thread instance that we’ll use 
				when writing videos to file (to avoid costly I/O latency delays).
		recording : Boolean value indicating whether or not we are in “recording mode”.

		frames : Video akışından en son okunan bufSize kareyi depolamak 
				için kullanılan bir önbellek.
		Q : Video dosyasına yazılacak kareleri bekleyen kareleri tutmak
		 	için kullanılan bir “ilk giren, ilk çıkan” (FIFO) Python Queue veri yapısı.
		writer : Aslında kareleri çıktı video dosyasına yazmak için 
			   kullanılan cv2.VideoWriter sınıfının bir örneği.
		thread : Video dosyalarını yazarken (maliyetli I/O gecikme gecikmelerinden kaçınmak için) 
				kullanacağımız bir Python Thread örneği.
		recording : “Kayıt modunda” olup olmadığımızı belirten Boolean değeri.
		"""

	def update(self, frame): 
		# update the frames buffer // kareleri güncelleyelim
		self.frames.appendleft(frame)  

		# if we are recording, update the queue as well // kayıt yapıyorsak, kuyruğu da güncelleyelim
		if self.recording:
			self.Q.put(frame)	

	# In order to kick-off an actual video clip recording, we need to define a start method:

	def start(self, outputPath, fourcc, fps):
		# indicate that we are recording, start the video writer,
		# and initialize the queue of frames that need to be written
		# to the video file
		self.recording = True
		self.writer = cv2.VideoWriter(outputPath, fourcc, fps,
			(self.frames[0].shape[1], self.frames[0].shape[0]), True)
		self.Q = Queue() # dosyaya yazılmaya hazır çerçeveleri depolamak 
		# için kullanılan Kuyruğumuzu başlatır. 
		# Daha sonra, çerçeve arabelleğimizdeki 
		# tüm çerçevelerin üzerinden geçer ve onları kuyruğa ekleriz. 

		# loop over the frames in the deque structure and add them
		# to the queue
		for i in range(len(self.frames), 0, -1):
			self.Q.put(self.frames[i - 1])

		# start a thread write frames to the video file
		self.thread = Thread(target=self.write, args=())
		self.thread.daemon = True
		self.thread.start()


	def write(self):
		# keep looping
		while True: 
			# if we are done recording, exit the thread
			if not self.recording:
				return
			
			# check to see if there are entries in the queue
			if not self.Q.empty(): # kuyrukta giriş var mı diye kontrol edelim
				# grab the next frame in the queue and write it
				# to the video file
				frame = self.Q.get() # kuyruktaki bir sonraki kareyi alalım ve video dosyasına yazalım
				self.writer.write(frame) 

			# otherwise, the queue is empty, so sleep for a bit
			# so we don't waste CPU cycles
			else: # aksi takdirde, kuyruk boş, bu yüzden biraz uyuyalım :)
				time.sleep(self.timeout)


	def flush(self): # boşaltmak
		# empty the queue by flushing all remaining frames to file
		while not self.Q.empty(): # kuyruk boş değilse
			frame = self.Q.get() # kuyruktaki bir sonraki kareyi alalım
			self.writer.write(frame) # ve video dosyasına yazalım

	"""Bu yöntem(flush), bir video kaydı bittiğinde kullanılır ve hemen tüm kareleri dosyaya boşaltmamız gerekir."""

	def finish(self):
		# indicate that we are done recording, join the thread,
		# flush all remaining frames in the queue to file, and
		# release the writer pointer
		self.recording = False # kayıt bitti
		self.thread.join() # thread birleştir
		self.flush() # kuyruğu boşaltır
		self.writer.release() # writer işaretçisini serbest bırakır
		