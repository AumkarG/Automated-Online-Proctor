import cv2
import numpy as np
import cv2
import numpy as np
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from authenticate import authenticate
from imutils.video import VideoStream
import time
import os

def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    return keypoints


def generate_eyes(landmarks,frame):
    x1=landmarks[36][0]
    x2=landmarks[39][0]
    y1=max(landmarks[37][1],landmarks[38][1])
    y2=min(landmarks[40][1],landmarks[41][1])
    x3=landmarks[42][0]
    x4=landmarks[45][0]
    y3=max(landmarks[43][1],landmarks[44][1])
    y4=min(landmarks[46][1],landmarks[47][1])   
    w1=x2-x1
    h1=y2-y1
    w2=x4-x3
    h2=y4-y3
    leye=frame[y1-h1:y2+h1,x1-w1//4:x2+w1//4]
    reye=frame[y3-h2:y4+h2,x3-w2//4:x4+w2//4]
    return leye,reye