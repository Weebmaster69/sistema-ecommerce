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