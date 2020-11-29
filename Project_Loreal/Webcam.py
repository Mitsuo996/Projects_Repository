# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 384)
cam.set(4, 384)


class Webcam(QObject) : #Communication between Python and Qt

    #Signal send to the interface
    userImage = pyqtSignal(str, arguments=['user_image_tx'])

    count = False

    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(int)
    def capture(self,camera_shot):
        self.trigger = 0
        self.trigger = camera_shot

    #Signals conected to the interface
    @pyqtSlot(int)
    def image(self,active):
            self.count = not self.count
            while True:
                if not cam.isOpened():
                    cam.open(0)
                    cam.set(3, 384)
                    cam.set(4, 384)
                ret, frame = cam.read()
                if not ret:
                    print("Failed to Grab Frame")
                    break
                cv2.imshow("Camara", frame)
                cv2.resizeWindow('Resized Window', 384, 384)

                k = cv2.waitKey(1)
                if k%256 == 32:
                    # SPACE pressed
                    image_name = "camera_image"+str(self.count)+".jpg"
                    cv2.imwrite(image_name, frame)
                    print("Capture")
                    break

            cam.release()
            cv2.destroyAllWindows()

            self.userImage.emit(image_name)



