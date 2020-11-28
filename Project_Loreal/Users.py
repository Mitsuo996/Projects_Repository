# This Python file uses the following encoding: utf-8
from PySide2.QtCore import Slot,QObject

class User:
    age = 0
    gender = ""
    location = ""
    image = ""


class Users(QObject) : #Communication between Python and Qt

    list_users = {}
    active_user = ""

    def __init__(self):
        QObject.__init__(self)

    def update_user(self):
        print("============================================")
        print("User: ",self.active_user)
        print("Age: ",self.list_users[self.active_user].age)
        print("Gender: ",self.list_users[self.active_user].gender)
        print("Location: ",self.list_users[self.active_user].location)
        print("Image: ",self.list_users[self.active_user].image)
        print("============================================")

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

        return self.active_user

    #Signals received from the interface
    @Slot(str)
    def set_Gender(self,gender):
        self.list_users[self.active_user].gender = gender

    @Slot(str)
    def set_patient_name(self,name):
        result = self.load_User(name)
        print(result)

    @Slot(str)
    def set_patient_age(self,age):
      self.list_users[self.active_user].age = age

    @Slot(str)
    def set_location(self,body_part):
      self.list_users[self.active_user].location = body_part

