import csv
from ui.menu_admin import MenuAdmin

class Login:
    ESPACIOS = 60
    RUTA_ADMINS = "config/admins.csv"

    def imprimir_menu(self):
        print("-" * self.ESPACIOS)
        print("INICIO DE SESION DE USUARIOS".center(self.ESPACIOS))
        print("-" * self.ESPACIOS)

    @staticmethod
    def recoger_usuario_contra():
        usuario = input("Usuario: ").lower()
        contra = input("Contraseña: ")
        return usuario, contra

    @staticmethod
    def verificar_credenciales(usuario, contra, archivo):
        try:
            with open(archivo, newline='', encoding='utf-8') as csvfile:
                lector = csv.reader(csvfile)
                for fila in lector:
                    if len(fila) >= 2 and fila[0] == usuario and fila[1] == contra:
                        return True
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
        return False

    def tratar_opcion(self, usuario, contra):
        if self.verificar_credenciales(usuario, contra, self.RUTA_ADMINS):
            print("Login correcto. Accediendo al menú de administración...")
            MenuAdmin().main()
        else:
            print("Usuario o Contraseña Incorrectos.")

    def login(self):
        self.imprimir_menu()
        usuario, contra = self.recoger_usuario_contra()
        self.tratar_opcion(usuario, contra)