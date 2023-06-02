from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

import Funciones as Func

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")
back = os.path.join(BASE_DIR, "Resources\\fondo.png")
cuadro_Trans = os.path.join(BASE_DIR, "Resources\\cuadroTrans.png")
logo_SS = os.path.join(BASE_DIR, "Resources\\SS_Logo.png")

#app = QApplication([])

class VentanaModificar(QMainWindow):
    def __init__(self, parent = None, *args):
        super(VentanaModificar, self).__init__(parent = None)

        self.Id = None
        self.Precio = None
        self.Nombre = None
        self.Desc = None
        self.Stock = None

        self.setFont(QFont('arial', 20))
        self.setFixedSize(1280,720)
        self.setWindowTitle("Modificar")

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

        texto = QLabel("Ingrese la ID del producto a modificar: ", self)
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

        self.inputNombre = QLabel(self. Nombre, self)
        self.inputNombre.setGeometry(250, 455, 300, 45)

        self.inputDesc = QLabel(self.Desc ,self)
        self.inputDesc.setGeometry(600, 455, 300, 145)

        self.inputStock = QLineEdit(self)
        self.inputStock.setGeometry(250, 555, 300, 45)
        self.inputStock.setClearButtonEnabled(True)

        self.btn = QPushButton("Modificar", self)
        self.btn.setGeometry(950, 455, 150, 50)
        self.btn.clicked.connect(lambda: self.modificar())

        self.btn2 = QPushButton("<<", self)
        self.btn2.setGeometry(50, 50, 60, 60)
        self.btn2.clicked.connect(lambda: self.AbrirMenu())

    def modificar(self):
        self.Id = self.inputID.text()
        self.Precio = self.inputPrecio.text()
        self.Stock = self.inputStock.text()
        parametros = (self.Stock, self.Precio, self.Id)
        query = "UPDATE Producto SET stock = ?, precio = ? WHERE id = ?"
        self.consultar(query, parametros)
        QMessageBox.question(self, 'LISTO', "El producto se modifico correctamente de la base de datos", QMessageBox.Ok)

    def consultar(self, query, parameters = ()):
        with sql.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def AbrirMenu(self):
        self.close()
        window = Func.VentanaMenu()
        window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = VentanaModificar()
    window.show()
    app.exec_()