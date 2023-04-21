user = 'usuario'
pasw = 'contra'

class LoginP():

    def ingreso(self):
        print("El ingreso ha sido exitoso.")

    def comparacion(self, a, b):
        if str(a) == user and str(b) == pasw:
            self.ingreso()
            return 1
        else:
            print("El ingreso no ha sido exitoso.")
            return 0;

    def login(self):
        in1 = input("Ingrese el usuario: ")
        in2 = input("Ingrese la contraseña: ")
        a = self.comparacion(in1, in2)
        if a == 1:
            print("Bienvenido")

a = LoginP()
a.login()