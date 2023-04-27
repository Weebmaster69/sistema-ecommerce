import sqlite3 as sql

class FuncionesDB():
    def verificarCredenciales(self):
        band = False
        band2 = False
        query = "SELECT usuario From credenciales"
        creds = self.consultar(query)
        for cred in creds:
            verificacion = ''.join(str(i) for i in cred)
            if (str(verificacion) == self.usuario):
                band = True 

        query = "SELECT contrasena from credenciales"
        creds = self.consultar(query)
        for cred in creds:
            verificacion = ''.join(str(i) for i in cred)
            if (str(verificacion) == self.contrasena):
                band2 = True 
        
        if band and band2:
            return True
        else:
            return False
        
class AgregarProducto():
    def agregarProducto(self):
        self.codigo =  int(input("Ingrese el codigo del nuevo libro: "))
        self.nombre =  str(input("Ingrese el nombre del nuevo libro: "))    
        self.autor = str(input("Ingresar el autor del nuevo libro: "))
        self.stock = int(input("Ingresar el stock del nuevo libro: "))
        Verificacion = Funciones_Admin_Db.VerificarCodigo(self)
        if (self.codigo > 0 and len(self.nombre) != 0 and len(self.autor) != 0 and self.stock > 0) and (isinstance(self.codigo, int) and (self.nombre, str) and self.autor.isdigit() != True and isinstance(self.stock, int)) and Verificacion == True :
            Funciones_Admin_Db.agregarProductos(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        VolverMenuPrincipal.volverMenu(self)