import sqlite3 as sql

from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")

class VentanaAnadir(QMainWindow):
    def __init__(self, parent = None, *args):
        super(VentanaAnadir, self).__init__(parent = None)

        self.Id = None
        self.Precio = None
        self.Nombre = None
        self.Desc = None
        self.Stock = None

        self.setFixedSize(1280,720)
        self.setWindowTitle("Login")

        label = QLabel("ID: ", self)
        label.setGeometry(50, 50, 100, 100)

        label1 = QLabel("Precio: ", self)
        label1.setGeometry(200, 50, 100, 100)

        label2 = QLabel("Nombre: ", self)
        label2.setGeometry(50, 110, 100, 100)

        label3 = QLabel("Descripcion: ", self)
        label3.setGeometry(200, 110, 100, 100)

        label4 = QLabel("Stock: ", self)
        label4.setGeometry(50, 170, 100, 100)

        self.inputID = QLineEdit(self)
        self.inputID.setGeometry(50, 115, 100, 25)
        self.inputID.setClearButtonEnabled(True)
        self.inputID.returnPressed.connect(self.show_text)

        self.inputPrecio = QLineEdit(self)
        self.inputPrecio.setGeometry(200, 115, 100, 25)
        self.inputPrecio.setClearButtonEnabled(True)
        self.inputPrecio.returnPressed.connect(self.show_text)

        self.inputNombre = QLineEdit(self)
        self.inputNombre.setGeometry(50, 175, 100, 25)
        self.inputNombre.setClearButtonEnabled(True)
        self.inputNombre.returnPressed.connect(self.show_text)

        self.inputDesc = QLineEdit(self)
        self.inputDesc.setGeometry(200, 175, 100, 85)
        self.inputDesc.setClearButtonEnabled(True)
        self.inputDesc.returnPressed.connect(self.show_text)

        self.inputStock = QLineEdit(self)
        self.inputStock.setGeometry(50, 235, 100, 25)
        self.inputStock.setClearButtonEnabled(True)
        self.inputStock.returnPressed.connect(self.show_text)

        self.btn = QPushButton("Agregar", self)
        self.btn.setGeometry(330, 150, 100, 50)
        
        self.btn.clicked.connect(lambda: self.agregar())

    def show_text(self):
        self.Id = self.inputID.text()
        self.Precio = self.inputPrecio.text()
        self.Nombre = str(self.inputNombre.text())
        self.Desc = str(self.inputDesc.text())
        self.Stock = self.inputStock.text()

    def consultar(self, query, parameters = ()):
        with sql.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def agregar(self):
        query = 'INSERT or IGNORE INTO Producto VALUES(?, ?, ?, ?, ?)'
        parametros = (self.Id, self.Precio, self.Nombre, self.Desc, self.Stock)
        self.consultar(query, parametros)
        print("Los datos han sido guardados.")

    
if __name__ == '__main__':
    app = QApplication([])
    window = VentanaAnadir()
    window.show()
    app.exec_()