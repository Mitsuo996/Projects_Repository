# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from Users import User
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

    def __init__(self,Users):
        QObject.__init__(self)
        self.input_users = Users

    model_path = "./Models/Model1.h5"

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

    def predict_model():
        pass

    def train_model():
        pass

    @pyqtSlot(str)
    def search_result(self,arg):
      print("===========================================")
      print("Model: Start")
      if self.verify_inputs() == True:
          #Preprocess Image
          #Load Image
          #Send Result
          pass
      else:
          pass


