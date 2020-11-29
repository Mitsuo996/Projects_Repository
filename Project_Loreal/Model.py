# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from Users import User

from keras.models import load_model
import keras
import tensorflow

class Model(QObject):

    def __init__(self,Users):
        QObject.__init__(self)
        self.input_users = Users

    model_path = "./Models/classification_model.h5"

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
        print("============================================")

    def predict_model():
        pass

    def train_model():
        pass

    @pyqtSlot(str)
    def search_result(self,arg):
      print("===========================================")
      print("Model: Start")
      self.verify_inputs()


