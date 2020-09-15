import cv2
import numpy as np
from imutils import face_utils
import argparse
import imutils
import dlib
from win32api import GetSystemMetrics
from imutils.video import VideoStream
import time
import os


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")



def main():
        frame = cv2.imread('D:\Downloads\\eg8.v1.jpg')
      #  print(frame)
        detect=detector(frame,1)                    # get faces from DLIB
        if(len(detect)==0):
            print('Candidate not found !')
        elif(len(detect)>1):
            print('More than one person observed')
        else:
            print('Candidate found')
            face=detect[0]
            landmarks=predictor(frame,face)
            coords = np.zeros((68, 2), dtype=int)
            for i in range(0, 68):
                coords[i] = (landmarks.part(i).x, landmarks.part(i).y)
                # loop over the face parts individually
        frame[1==1]=255
        t=1
        for x in coords:
            if(t==61 or t==63 or t==65 or t==67):
                frame = cv2.circle(frame, (x[0],x[1]), radius=2, color=(0, 0 , 255), thickness=-1)
            else:
                frame = cv2.circle(frame, (x[0],x[1]), radius=2, color=(0, 0, 0), thickness=-1)

            font = cv2.FONT_HERSHEY_SIMPLEX 
            
            org = (x[0]+2,x[1]+2) 
            
            fontScale = 0.25
            
            color = (0, 0, 0) 
            
            thickness = 0
            
            if(t==61 or t==63 or t==65 or t==67):
                if(t==61):
                    s="p3"
                elif(t==63):
                    s="p1"
                elif(t==65):
                    s="p2"
                else:
                    s="p4"
                frame = cv2.putText(frame,s, org, font,  fontScale, color, thickness, cv2.LINE_AA)
            t+=1

        print(frame)
        print(frame.shape)
        cv2.imwrite('face.jpg',frame)
        cv2.imshow('x',frame)
        cv2.waitKey(0)


if __name__ == "__main__":
    main()
