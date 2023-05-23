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

class VentanaEliminar(QMainWindow):
    def __init__(self, parent = None, *args):
        super(VentanaEliminar, self).__init__(parent = None)

        self.Id = None

        self.setFont(QFont('arial', 20))
        self.setFixedSize(1280,720)
        self.setWindowTitle("Eliminar")

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

        label = QLabel("ID: ", self)
        label.setGeometry(250, 280, 100, 100)

        self.inputID = QLineEdit(self)
        self.inputID.setGeometry(250, 355, 300, 45)
        self.inputID.setClearButtonEnabled(True)
        self.inputID.returnPressed.connect(self.show_text)

        self.btn = QPushButton("Eliminar", self)
        self.btn.setGeometry(950, 455, 150, 50)
        self.btn.clicked.connect(lambda: self.eliminar())
        
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

    def eliminar(self):
        self.Id = self.inputID.text()
        parametros = self.Id
        query = 'DELETE FROM Producto WHERE Id = ?'
        self.consultar(query, [parametros])
        print(self.Id)
        QMessageBox.question(self, 'LISTO', "El producto se elimino correctamente de la base de datos", QMessageBox.Ok)

    def AbrirMenu(self):
        self.close()
        window = Func.VentanaMenu()
        window.show()