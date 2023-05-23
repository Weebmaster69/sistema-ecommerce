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

app = QApplication([])

class VentanaListarProductos(QMainWindow):
    def __init__(self, parent=None, *args):
        super(VentanaListarProductos, self).__init__(parent=None)

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

        label = QLabel("Lista de todos los productos: ", self)
        label.setGeometry(100, 220, 400, 100)

        self.btn2 = QPushButton("<<", self)
        self.btn2.setGeometry(50, 50, 60, 60)
        self.btn2.clicked.connect(lambda: self.AbrirMenu())

        # Crear la tabla para mostrar los productos
        self.tablaProductos = QTableWidget(self)
        self.tablaProductos.setGeometry(100, 300, 1100, 360)
        self.tablaProductos.setColumnCount(5)
        self.tablaProductos.setHorizontalHeaderLabels(["ID", "Nombre", "Stock", "Descripción", "Precio"])
        self.tablaProductos.setColumnWidth(0, 5)
        self.tablaProductos.setColumnWidth(1, 350)
        self.tablaProductos.setColumnWidth(2, 15)
        self.tablaProductos.setColumnWidth(3, 465)
        self.tablaProductos.setColumnWidth(4, 100)

        # Llenar la tabla con los productos
        self.listarProductos()

    def listarProductos(self):
        # Consultar la base de datos y llenar la tabla
        query = "SELECT * FROM Producto"
        productos = self.consultar(query)
        self.tablaProductos.setRowCount(len(productos))
        for i, producto in enumerate(productos):
            self.tablaProductos.setItem(i, 0, QTableWidgetItem(str(producto[0])))
            self.tablaProductos.setItem(i, 1, QTableWidgetItem(producto[1]))
            self.tablaProductos.setItem(i, 2, QTableWidgetItem(str(producto[2])))
            self.tablaProductos.setItem(i, 3, QTableWidgetItem(producto[3]))
            self.tablaProductos.setItem(i, 4, QTableWidgetItem(str(producto[4])))

    def consultar(self, query, parameters=()):
        with sql.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters)
            result = cursor.fetchall()
        return result
    
    def AbrirMenu(self):
            self.close()
            window = Func.VentanaMenu()
            window.show()