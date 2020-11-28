# This Python file uses the following encoding: utf-8
from PySide2.QtCore import Slot,QObject
import cv2

cam = cv2.VideoCapture(0)
counter = 0

class Webcam:
    def __init__(self):
        self.image = 0

class Webcam(QObject) : #Communication between Python and Qt
    def __init__(self):
        QObject.__init__(self)

    #Signals conected to the interface
    @Slot(int)
    def image(self,active):
        active = active + counter;
        if active == 1:
            while True:
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








