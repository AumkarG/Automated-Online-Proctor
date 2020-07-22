import os
import cv2
import dlib
from Align import AlignDlib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
import tensorflow as tf
from joblib import dump, load
from sklearn.metrics import f1_score, accuracy_score
import time
import os.path
from keras.models import load_model
import tensorflow as tf
from keras.models import Model
import pickle

# load model
m=Model()

m = load_model('mod.h5',custom_objects={'tf': tf})

a_file = open("data.pkl", "rb")
embeddings = pickle.load(a_file)


  
def align_image(img,detector,predictor):
    alignment = AlignDlib(detector,predictor)
    return alignment.align(96, img, alignment.getLargestFaceBoundingBox(img), 
                           landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

def embed(img,detector,predictor):
    img = align_image(img,detector,predictor)
    img = (img / 255.).astype(np.float32)
    emb = m.predict(np.expand_dims(img, axis=0))[0]
    return emb

def distance(emb1, emb2):
    return np.sum(np.square(emb1 - emb2))

def authenticate(frame,name,detector,predictor):
    emb1=embeddings[name]
    emb2=embed(frame,detector,predictor)
    d=distance(emb1,emb2)
    print(d)
    if(d<0.5):
        print('authenticated!')
        return True
    else:
        return False
    


