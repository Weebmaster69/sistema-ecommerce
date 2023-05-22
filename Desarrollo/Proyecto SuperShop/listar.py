from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

import Funciones as Func

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")

class VentanaListarProductos(QMainWindow):
    def __init__(self, parent=None, *args):
        super(VentanaListarProductos, self).__init__(parent=None)

        self.setFont(QFont('arial', 20))
        self.setFixedSize(1280,720)
        self.setWindowTitle("Login")

        self.btn2 = QPushButton("<<", self)
        self.btn2.setGeometry(50, 50, 60, 60)
        self.btn2.clicked.connect(lambda: self.AbrirMenu())

        # Crear la tabla para mostrar los productos
        self.tablaProductos = QTableWidget(self)
        self.tablaProductos.setGeometry(10, 10, 620, 460)
        self.tablaProductos.setColumnCount(5)
        self.tablaProductos.setHorizontalHeaderLabels(["ID", "Nombre", "Stock", "Descripción", "Precio"])

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

if __name__ == '__main__':
   app = QApplication([])
   window = VentanaListarProductos()
   window.show()
   app.exec_()
