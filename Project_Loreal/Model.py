# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from Users import User
from Webcam import Webcam

from keras.models import load_model
import keras
import pandas as pd
import numpy as np
import os
import random
import re
import math
import time
from tqdm import tqdm
from tqdm.keras import TqdmCallback
import warnings
import tensorflow as tf
import tensorflow.keras.backend as K
import efficientnet.tfkeras as efn

class Model(QObject):

    #Signal send to the interface
    userResult = pyqtSignal(str, arguments=['user_result_tx'])

    def __init__(self,Users,Webcam):
        QObject.__init__(self)
        self.input_users = Users
        self.input_camera = Webcam

    model_path = "./Models/LorealEffNetB3.h5"

    def load_model(self):
        self.model = load_model(self.model_path)
        print("===========================================")
        print("Model Loaded")
        print(self.model)


    def verify_inputs(self):
        print("==============Verification==================")
        print("Age: ",self.input_users.list_users[self.input_users.active_user].age)
        print("Gender: ",self.input_users.list_users[self.input_users.active_user].gender)
        print("Location: ",self.input_users.list_users[self.input_users.active_user].location)
        print("Image: ",self.input_users.list_users[self.input_users.active_user].image)
        print("===========================================")


        if(self.input_users.list_users[self.input_users.active_user].image !=""):
            print('Valid Input')
            return True
        else:
            print('Invalid Input: No image detected')
            return False

    def predict_model(self):

        #Read image name
        image = tf.io.read_file("camera_image"+str(self.input_camer.count)+".jpg")
        image = tf.io.decode_jpeg(image, channels = 3)
        image = tf.image.resize(image, [384,384],antialias=True)
        image = tf.cast(image, tf.float32)/255
        image = tf.image.random_flip_left_right(image)
        image = tf.image.random_saturation(image, 0.7, 1.3)
        image = tf.image.random_contrast(image, 0.8, 1.2)
        image = tf.image.random_brightness(image, 0.1)

        result = self.model.predict(np.array([image,]))
        print (result[0][0])
        if result[0][0] > 0.5:
            self.userResult.emit("maligno")
            print ("maligno")
        else:
            self.userResult.emit("benigno")
            print("benigno")


    @pyqtSlot(str)
    def search_result(self,arg):
      print("===========================================")
      print("Model: Start")
      self.predict_model()


