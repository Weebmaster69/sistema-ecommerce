from BaseDatos.FuncionesDB import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "BaseDatos\\producto.db")

class VentanaEliminar(QMainWindow):
    def __init__(self, parent = None, *args):
        super(VentanaEliminar, self).__init__(parent = None)

        self.Id = None

        self.setFixedSize(1280,720)
        self.setWindowTitle("Login")

        label = QLabel("ID: ", self)
        label.setGeometry(50, 50, 100, 100)

        self.inputID = QLineEdit(self)
        self.inputID.setGeometry(50, 115, 100, 25)
        self.inputID.setClearButtonEnabled(True)
        self.inputID.returnPressed.connect(self.show_text)

        self.btn = QPushButton("Eliminar", self)
        self.btn.setGeometry(330, 150, 100, 50)
        
        self.btn.clicked.connect(lambda: self.eliminar())

    def show_text(self):
        self.Id = self.inputID.text()

    def consultar(self, query, parameters = ()):
        with sql.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def eliminar(self):
        query = 'DELETE FROM Producto WHERE Id = ?'
        parametros = (self.Id,)
        self.consultar(query, parametros)
        print("El registro ha sido eliminado.")

    
if __name__ == '__main__':
    app = QApplication([])
    window = VentanaEliminar()
    window.show()
    app.exec_()
