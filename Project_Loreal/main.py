# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5.QtGui  import QGuiApplication
from PyQt5.QtQml  import QQmlApplicationEngine

from Users import Users
from Model import Model
from Webcam import Webcam


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    #Object instances
    engine = QQmlApplicationEngine()
    Users = Users()
    webcam = Webcam()
    model = Model(Users)

    model.load_model()
    engine.rootContext().setContextProperty("user", Users)
    engine.rootContext().setContextProperty("webcam",webcam)
    engine.rootContext().setContextProperty("app_model",model)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())

