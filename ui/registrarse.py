from ui.login import Login

class Registro:
    ESPACIOS: int = 60

    def imprimir_menu(self):
        print("-" * self.ESPACIOS)
        print("REGISTRO USUARIOS".center(self.ESPACIOS))
        print("-" * self.ESPACIOS)
        print("¡¡¡IMPORTANTE!!!")
        print("Si usted se desea registrar en la página web, pida en su centro su contraseña y usuario.")

    @staticmethod
    def recoger_opcion() -> str:
        while True:
            opcion = input("¿Se quiere registrar usted? (S/N): ").upper()
            if opcion in ("S", "N"):
                return opcion
            else:
                print("Error, introduzca una opción válida (S o N).")

    @staticmethod
    def tratar_opcion( opcion: str):
        match opcion:
            case "S":
                Login()
            case "N":
                print("Hasta pronto, vuelva cuando quiera.")
            case _:
                print("Error inesperado.")

    def registrarse(self):
        self.imprimir_menu()
        opcion = self.recoger_opcion()
        self.tratar_opcion(opcion)