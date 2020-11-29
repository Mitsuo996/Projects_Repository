# This Python file uses the following encoding: utf-8

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
class User:
    age = 0
    gender = ""
    location = ""
    image = ""


class Users(QObject) : #Communication between Python and Qt

    #Signal send to the interface
    textResult = pyqtSignal(str, arguments=['user_gender_tx'])

    list_users = {"":User()}
    active_user = ""

    def __init__(self):
        QObject.__init__(self)

    #Signals received from the interface
    @pyqtSlot(str)
    def set_Gender(self,gender):
        self.list_users[self.active_user].gender = gender

    @pyqtSlot(str)
    def set_patient_name(self,name):
        result = self.load_User(name)

    @pyqtSlot(str)
    def set_patient_age(self,age):
        self.list_users[self.active_user].age = age

    @pyqtSlot(str)
    def set_location(self,body_part):
        self.list_users[self.active_user].location = body_part

    def update_user(self):
        print("============================================")
        print("User: ",self.active_user)
        print("Age: ",self.list_users[self.active_user].age)
        print("Gender: ",self.list_users[self.active_user].gender)
        print("Location: ",self.list_users[self.active_user].location)
        print("Image: ",self.list_users[self.active_user].image)
        print("============================================")
        self.textResult.emit('Patient = '+self.list_users[self.active_user].gender)



    def load_User(self,user_name):

        if user_name in self.list_users:
            print("This User already Exist, conected to this user")
            self.active_user = user_name
            self.update_user()
        else:
            new_user = User()
            self.list_users[user_name] = new_user

            print("New user added: ",user_name)
            self.active_user = user_name



