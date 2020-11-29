# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
import cv2

cam = cv2.VideoCapture(0)

class Webcam:
    def __init__(self):
        self.image = 0
        self.capture = 0

class Webcam(QObject) : #Communication between Python and Qt
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(int)
    def capture(self,camera_shot):
        self.trigger = 0
        self.trigger = camera_shot

    #Signals conected to the interface
    @pyqtSlot(int)
    def image(self,active):
        if active == 1:
            while True:
                #print (self.trigger)
                ret, frame = cam.read()
                if not ret:
                    print("Failed to Grab Frame")
                    break
                cv2.imshow("Camara", frame)
                cv2.resizeWindow('Resized Window', 400, 650)

                k = cv2.waitKey(1)
                if k%256 == 32:
                    # SPACE pressed
                    cv2.imwrite("image.png", frame)
                    print("Capture")
                    break

            cam.release()
            cv2.destroyAllWindows()

