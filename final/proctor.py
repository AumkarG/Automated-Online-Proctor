from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from win32api import GetSystemMetrics
from imutils.video import VideoStream
import time
import os
from argparse import ArgumentParser
from pose_estimator import PoseEstimator
from eye import blob_process,generate_eyes 
from authenticate import authenticate

detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detectorb = cv2.SimpleBlobDetector_create(detector_params)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


parser = ArgumentParser()
parser.add_argument("--video", type=str, default=None,
                    help="Video file to be processed.")
parser.add_argument("--cam", type=int, default=None,
                    help="The webcam index.")
args = parser.parse_args()



def main():
    video_src = args.cam if args.cam is not None else args.video
    if video_src is None:
        print("Warning: video source not assigned, default webcam will be used.")
        video_src = 0

    cap = cv2.VideoCapture(video_src)
    if video_src == 0:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    sample_frame=None

    while True:
        _, sample_frame = cap.read()
        cv2.imshow("test", sample_frame)
        k = cv2.waitKey(1)
        if k%256 == 32:
            break

    cap.release()
    cv2.destroyAllWindows()
    if(authenticate(sample_frame,"aumkar",detector,predictor)):      
        height, width = sample_frame.shape[:2]
        pose_estimator = PoseEstimator(img_size=(height, width))
        cap = cv2.VideoCapture(video_src)
        if video_src == 0:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        while True:
            frame_got, frame = cap.read()
            if frame_got is False:
                break
            detect=detector(frame,1)                   
            if(len(detect)==0):
                print('CANDIDATE NOT FOUND')
            elif(len(detect)>1):
                print("Multiple faces detected")
            else:
                landmarks=predictor(frame,detect[0])
                landmarks = face_utils.shape_to_np(landmarks)
                if landmarks is not None: 
                    landmarks=np.array(landmarks)
                    marks=landmarks.astype('float32')
                    try :
                        pose = pose_estimator.solve_pose_by_68_points(marks)
                     #   print(pose)
                        pose_estimator.draw_annotation_box(frame, pose[0], pose[1], color=(255, 128, 128))
                        pose_estimator.draw_axes(frame, pose[0], pose[1])                 
                    except Exception as e:
                        print(e)
                    leye,reye = generate_eyes(landmarks,frame)
                    threshold=52
                    keypoints = blob_process(leye, threshold, detectorb)
                    print(keypoints)
                    reye = cv2.drawKeypoints(reye, keypoints, leye, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    keypoints = blob_process(reye, threshold, detectorb)
                    print(keypoints)
                    reye = cv2.drawKeypoints(reye, keypoints, reye, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            cv2.imshow("Preview", frame)
            if cv2.waitKey(10) == 27:
                break
    else:
        print("NOT IDENTIFIED")
if __name__ == '__main__':
    main()


i