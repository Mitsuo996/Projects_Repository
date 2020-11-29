# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
import sqlite3
from Users import User

class Database(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.conn = sqlite3.connect('melanoma.db')

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS submits(id INTEGER PRIMARY KEY AUTOINCREMENT,
                              Name text,
                              Age integer,
                              Gender text,
                              Location text,
                              Diagnosis text);''')

    def add_user(self,User):
        patient_name= User.name
        age = User.age
        gender = User.gender
        location = User.location
        diagnosis = User.result

        self.conn.execute("INSERT into submits(Name,Age,Gender,Location,Diagnosis) values (?,?,?,?,?)", (patient_name,age,gender,location,diagnosis))
        self.conn.commit()

        cursor = self.conn.execute(''' SELECT *
                                  FROM submits;''')
        for row in cursor:
          print(row)
        self.conn.close()

    #def search_user(self):



