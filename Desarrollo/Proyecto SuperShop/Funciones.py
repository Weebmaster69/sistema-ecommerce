import sqlite3 as sql

from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")
back = os.path.join(BASE_DIR, "Resources\\fondo.png")
cuadro_Trans = os.path.join(BASE_DIR, "Resources\\cuadroTrans.png")
logo_Bertell = os.path.join(BASE_DIR, "Resources\\Bertell_Logo.png")
logo_SS = os.path.join(BASE_DIR, "Resources\\SS_Logo.png")

app = QApplication([])

import listar as List
import eliminar as Elim
import modificar as Mod
import genReporte as Gen

class VentanaMenu(QMainWindow):
    def __init__(self, parent = None, *args):
        super(VentanaMenu, self).__init__(parent = None)

        self.setFont(QFont('arial', 20))
        self.setFixedSize(1280,720)
        self.setWindowTitle("Menu")

        background = QLabel(self)
        background1 = QPixmap(back).scaledToWidth(1400)
        background.setGeometry(0,0,background1.width(),background1.height()-40)
        background.setPixmap(background1)

        cuadroTrans = QLabel(self)
        cuadroTrans1 = QPixmap(cuadro_Trans).scaledToHeight(1400)
        cuadroTrans.setGeometry(0,225,cuadroTrans1.width(),cuadroTrans1.height()-930)
        cuadroTrans.setPixmap(cuadroTrans1)

        logoBertell = QLabel(self)
        logoBertell1 = QPixmap(logo_Bertell).scaledToWidth(200)
        logoBertell.setGeometry(30,25,logoBertell1.width(),logoBertell1.height())
        logoBertell.setPixmap(logoBertell1)

        logoSS = QLabel(self)
        logoSS1 = QPixmap(logo_SS).scaledToWidth(850)
        logoSS.setGeometry(200,40,logoSS1.width(),logoSS1.height())
        logoSS.setPixmap(logoSS1)

        label = QLabel("Bienvenido que desea hacer hoy: ", self)
        label.setGeometry(150, 230, 400, 100)

        self.btn = QPushButton("Añadir Productos", self)
        self.btn.setGeometry(300, 350, 300, 50)
        self.btn.clicked.connect(lambda: self.AbrirAnadir())

        self.btn2 = QPushButton("Eliminar Producto", self)
        self.btn2.setGeometry(300, 450, 300, 50)
        self.btn2.clicked.connect(lambda: self.AbrirEliminar())

        self.btn3 = QPushButton("Modificar Producto", self)
        self.btn3.setGeometry(300, 550, 300, 50)
        self.btn3.clicked.connect(lambda: self.AbrirMod())

        self.btn4 = QPushButton("Generar Reporte", self)
        self.btn4.setGeometry(720, 400, 300, 50)
        self.btn4.clicked.connect(lambda: self.AbrirGen())

        self.btn5 = QPushButton("Listar Producto", self)
        self.btn5.setGeometry(720, 500, 300, 50)
        self.btn5.clicked.connect(lambda: self.AbrirLista())

    def AbrirAnadir(self):
        self.close()
        window = VentanaAnadir()
        window.show()

    def AbrirEliminar(self):
        self.close()
        window = Elim.VentanaEliminar()
        window.show()

    def AbrirMod(self):
        self.close()
        window = Mod.VentanaModificar()
        window.show()

    def AbrirGen(self):
        self.close()
        window = Gen.VentanaReporte()
        window.show()

    def AbrirLista(self):
        self.close()
        window = List.VentanaListarProductos()
        window.show()
        
class VentanaAnadir(QMainWindow):
    def __init__(self, parent = None, *args):
        super(VentanaAnadir, self).__init__(parent = None)

        self.Id = None
        self.Precio = None
        self.Nombre = None
        self.Desc = None
        self.Stock = None

        self.setFont(QFont('arial', 20))
        self.setFixedSize(1280,720)
        self.setWindowTitle("Login")

        background = QLabel(self)
        background1 = QPixmap(back).scaledToWidth(1400)
        background.setGeometry(0,0,background1.width(),background1.height()-40)
        background.setPixmap(background1)

        cuadroTrans = QLabel(self)
        cuadroTrans1 = QPixmap(cuadro_Trans).scaledToHeight(1400)
        cuadroTrans.setGeometry(0,225,cuadroTrans1.width(),cuadroTrans1.height()-930)
        cuadroTrans.setPixmap(cuadroTrans1)

        logoSS = QLabel(self)
        logoSS1 = QPixmap(logo_SS).scaledToWidth(850)
        logoSS.setGeometry(200,40,logoSS1.width(),logoSS1.height())
        logoSS.setPixmap(logoSS1)

        texto = QLabel("Añadir Producto: ", self)
        texto.setGeometry(150, 230, 400, 100)

        label = QLabel("ID: ", self)
        label.setGeometry(250, 280, 100, 100)

        label1 = QLabel("Precio: ", self)
        label1.setGeometry(600, 280, 100, 100)

        label2 = QLabel("Nombre: ", self)
        label2.setGeometry(250, 380, 100, 100)

        label3 = QLabel("Descripcion: ", self)
        label3.setGeometry(600, 380, 300, 100)

        label4 = QLabel("Stock: ", self)
        label4.setGeometry(250, 480, 100, 100)

        self.inputID = QLineEdit(self)
        self.inputID.setGeometry(250, 355, 300, 45)
        self.inputID.setClearButtonEnabled(True)

        self.inputPrecio = QLineEdit(self)
        self.inputPrecio.setGeometry(600, 355, 300, 45)
        self.inputPrecio.setClearButtonEnabled(True)

        self.inputNombre = QLineEdit(self)
        self.inputNombre.setGeometry(250, 455, 300, 45)
        self.inputNombre.setClearButtonEnabled(True)

        self.inputDesc = QTextEdit(self)
        self.inputDesc.setGeometry(600, 455, 300, 145)

        self.inputStock = QLineEdit(self)
        self.inputStock.setGeometry(250, 555, 300, 45)
        self.inputStock.setClearButtonEnabled(True)

        self.btn = QPushButton("Agregar", self)
        self.btn.setGeometry(950, 455, 150, 50)
        self.btn.clicked.connect(lambda: self.agregar())

        self.btn2 = QPushButton("<<", self)
        self.btn2.setGeometry(50, 50, 60, 60)
        self.btn2.clicked.connect(lambda: self.AbrirMenu())

    def consultar(self, query, parameters = ()):
        with sql.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def agregar(self):
        self.Id = self.inputID.text()
        self.Precio = self.inputPrecio.text()
        self.Nombre = str(self.inputNombre.text())
        self.Desc = str(self.inputDesc.toPlainText())
        self.Stock = self.inputStock.text()

        if (len(self.Id) >0 or self.Id.isdigit() == True or len(self.Precio) >0 or self.Precio.isdigit() == True or len(self.Nombre) >0 or len(self.Stock) >0 or len(self.Stock) >0 or self.Stock.isdigit() == True):
            query = 'INSERT or IGNORE INTO Producto VALUES(?, ?, ?, ?, ?)'
            parametros = (self.Id, self.Nombre, self.Stock, self.Desc, self.Precio)
            self.consultar(query, parametros)
            QMessageBox.question(self, 'LISTO', "Se agrego el producto correctamente", QMessageBox.Ok)
        else:
            QMessageBox.question(self, 'ERROR', "Datos inválidos", QMessageBox.Ok)

    def AbrirMenu(self):
        self.close()
        window = VentanaMenu()
        window.show()
    
