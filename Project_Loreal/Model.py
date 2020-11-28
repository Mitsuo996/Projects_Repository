# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from Users import User

class Model(QtCore.QObject):

    def __init__(self):
        QObject.__init__(self)

    model_path = "/"

    def load_model(self):
        pass

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
