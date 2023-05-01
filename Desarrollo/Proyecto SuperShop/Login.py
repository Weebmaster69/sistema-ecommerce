import sqlite3 as sql

from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Funciones import*

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")



class LoginP(QMainWindow):

    def __init__(self, parent = None, *args):
        super(LoginP, self).__init__(parent = None)
        self.usuario = None
        self.contrasena = None

        self.setFont(QFont('arial', 20))
        self.setFixedSize(1280,720)
        self.setWindowTitle("Login")

        label = QLabel("Usuario: ", self)
        label.setGeometry(850, 250, 100, 100)

        label1 = QLabel("Pass: ", self)
        label1.setGeometry(850, 350, 100, 100)

        self.btn = QPushButton("Login", self)
        self.btn.setGeometry(900, 500, 200, 50)

        self.inputUser = QLineEdit(self)
        self.inputUser.setGeometry(850, 325, 300, 45)
        self.inputUser.setClearButtonEnabled(True)

        self.inputPass = QLineEdit(self)
        self.inputPass.setGeometry(850, 425, 300, 45)
        self.inputPass.setClearButtonEnabled(True)
        self.inputPass.setEchoMode(QLineEdit.Password)

        self.btn.clicked.connect(lambda: self.verificar())
        
    def consultar(self, query, parameters=()):
        with sql.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def verificar(self):
        self.usuario = str(self.inputUser.text())
        self.contrasena = str(self.inputPass.text())

        check = FuncionesDB.verificarCredenciales(self)
        if(check == True):
            self.close()
            window = VentanaMenu()
            window.show()
        else:
            QMessageBox.question(self, 'ERROR', "Usuario o contraseña Incorrecta", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication([])
    window = LoginP()
    window.show()
    app.exec_()