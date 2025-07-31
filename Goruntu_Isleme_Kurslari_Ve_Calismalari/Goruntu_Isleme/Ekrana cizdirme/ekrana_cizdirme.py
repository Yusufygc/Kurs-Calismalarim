import cv2
import numpy as np
from collections import deque



cap = cv2.VideoCapture(0)

lower_blue= np.array([100,60,60])
upper_blue= np.array([140,255,255])

blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

blue_index=0
green_index=0
red_index=0
yellow_index=0

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
color_index = 0
















