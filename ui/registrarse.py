from ui.login import Login

class Registro:
    ESPACIOS: int = 60

    def _imprimir_menu(self):
        print("-" * self.ESPACIOS)
        print("REGISTRO USUARIOS".center(self.ESPACIOS))
        print("-" * self.ESPACIOS)
        print("¡¡¡IMPORTANTE!!!")
        print("Si usted se desea registrar en la página web, pida en su centro su contraseña y usuario.")

    def _recoger_opcion(self) -> str:
        while True:
            opcion = input("¿Se quiere registrar usted? (S/N): ").upper()
            if opcion in ("S", "N"):
                return opcion
            else:
                print("Error, introduzca una opción válida (S o N).")

    def _tratar_opcion(self, opcion: str):
        match opcion:
            case "S":
                Login()
            case "N":
                print("Hasta pronto, vuelva cuando quiera.")
            case _:
                print("Error inesperado.")

    def _registrarse(self):
        self._imprimir_menu()
        opcion = self._recoger_opcion()
        self._tratar_opcion(opcion)