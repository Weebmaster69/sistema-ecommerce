import sqlite3 as sql

from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

from BaseDatos import FuncionesDB

from Funciones import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")
logo_Bertell = os.path.join(BASE_DIR, "Resources\\Bertell_Logo.png")
logo_SS = os.path.join(BASE_DIR, "Resources\\SS_Logo.png")
fondoSS = os.path.join(BASE_DIR, "Resources\\Supermercado.jpg")
cuadro = os.path.join(BASE_DIR, "Resources\\cuadro.png")
cuadro_Trans = os.path.join(BASE_DIR, "Resources\\cuadroTrans.png")
back = os.path.join(BASE_DIR, "Resources\\fondo.png")


class LoginP(QMainWindow):

    def __init__(self, parent = None, *args):
        super(LoginP, self).__init__(parent = None)
        self.usuario = None
        self.contrasena = None
        
        self.setFont(QFont('arial', 20))
        self.setFixedSize(1280,720)
        self.setWindowTitle("Login")

        background = QLabel(self)
        background1 = QPixmap(back).scaledToWidth(1400)
        background.setGeometry(0,0,background1.width(),background1.height())
        background.setPixmap(background1)

        fondo1 = QLabel(self)
        cuadro1 = QPixmap(cuadro).scaledToWidth(380)
        fondo1.setGeometry(860,300,cuadro1.width(),cuadro1.height()-40)
        fondo1.setPixmap(cuadro1)

        cuadroTrans = QLabel(self)
        cuadroTrans1 = QPixmap(cuadro_Trans).scaledToHeight(1400)
        cuadroTrans.setGeometry(0,225,cuadroTrans1.width(),cuadroTrans1.height()-930)
        cuadroTrans.setPixmap(cuadroTrans1)

        label = QLabel("Usuario: ", self)
        label.setGeometry(900, 300, 100, 100)

        label1 = QLabel("Pass: ", self)
        label1.setGeometry(900, 400, 100, 100)

        logoBertell = QLabel(self)
        logoBertell1 = QPixmap(logo_Bertell).scaledToWidth(200)
        logoBertell.setGeometry(30,25,logoBertell1.width(),logoBertell1.height())
        logoBertell.setPixmap(logoBertell1)

        label3 = QLabel(self)
        fondo = QPixmap(fondoSS).scaledToWidth(750)
        label3.setGeometry(50,250,fondo.width(),fondo.height())
        label3.setPixmap(fondo)

        logoSS = QLabel(self)
        logoSS1 = QPixmap(logo_SS).scaledToWidth(850)
        logoSS.setGeometry(425,25,logoSS1.width(),logoSS1.height())
        logoSS.setPixmap(logoSS1)

        self.btn = QPushButton("Login", self)
        self.btn.setGeometry(950, 550, 200, 50)

        self.inputUser = QLineEdit(self)
        self.inputUser.setGeometry(900, 375, 300, 45)
        self.inputUser.setClearButtonEnabled(True)

        self.inputPass = QLineEdit(self)
        self.inputPass.setGeometry(900, 475, 300, 45)
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