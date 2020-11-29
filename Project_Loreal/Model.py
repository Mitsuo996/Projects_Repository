# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from Users import User

from keras.models import load_model
import keras
import tensorflow

class Model(QtCore.QObject):

    def __init__(self):
        QtCore.QObject.__init__(self)

    model_path = "./Models/classification_model.h5"

    def load_model(self):
        self.model = load_model(self.model_path)
        print("===========================================")
        print("Model Loaded")
        print(self.models)


    def verify_inputs(user_input):
        print("==============Verification==================")
        print("Age: ",user_input.age)
        print("Gender: ",user_input.gender)
        print("Location: ",user_input.location)
        print("Image: ",user_input.image)
        print("============================================")

    def predict_model():
        pass

    def train_model():
        pass
