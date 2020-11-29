# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5.QtGui  import QGuiApplication
from PyQt5.QtQml  import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl

from Users import Users,User
from Model import Model
from Webcam import Webcam
from Database import Database

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    #Object instances
    engine = QQmlApplicationEngine()
    Users  = Users()
    webcam = Webcam()
    database = Database()
    model  = Model(Users,webcam,database)
    model.load_model()

    engine.rootContext().setContextProperty("user", Users)
    engine.rootContext().setContextProperty("webcam",webcam)
    engine.rootContext().setContextProperty("app_model",model)
    engine.rootContext().setContextProperty("database",database)

    engine.load(QUrl('main.qml'))

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())

