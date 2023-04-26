import sqlite3 as sql

from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")


class LoginP(QMainWindow):

    def __init__(self, parent = None, *args):
        super(LoginP, self).__init__(parent = None)
        self.usuario = None
        self.contrasena = None

        self.setFixedSize(300,200)
        self.setWindowTitle("Login")

        label = QLabel("Usuario: ", self)
        label.setGeometry(50, 50, 100, 100)

        label1 = QLabel("Pass: ", self)
        label1.setGeometry(50, 80, 100, 100)

        self.btn = QPushButton("Ingresar", self)
        self.btn.setGeometry(90, 145, 200, 50)

        self.inputUser = QLineEdit(self)

        self.inputUser.setGeometry(110, 84, 100, 25)
        self.inputUser.setClearButtonEnabled(True)
        self.inputUser.returnPressed.connect(self.show_text)

        self.inputPass = QLineEdit(self)
        self.inputPass.setGeometry(110, 114, 100, 25)
        self.inputPass.setClearButtonEnabled(True)
        self.inputPass.setEchoMode(QLineEdit.Password)
        self.inputPass.returnPressed.connect(self.show_text)

        self.btn.clicked.connect(lambda: self.verificar())

    def show_text(self):
        self.usuario = str(self.inputUser.text())
        self.contrasena = str(self.inputPass.text())

    def consultar(self, query, parameters=()):
        with sql.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def verificar(self):
        check = FuncionesDB.verificarCredenciales(self)
        if(check == True):
            print("Bienvenido al programa.")
        else:
            print("Reingrese las credenciales correctas.")

if __name__ == '__main__':
    app = QApplication([])
    window = LoginP()
    window.show()
    app.exec_()