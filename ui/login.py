from ui.menu_usuario import Menuusuario
from ui.menu_admin import Menuadmin

class Login:

    ESPACIOS: int = 60

    def _imprimir_menu(self):
        print("-" * self.ESPACIOS)
        print("INICIO DE SESION DE USUARIOS".center(self.ESPACIOS))
        print("-" * self.ESPACIOS)

    def _recoger_opcion(self) -> str:
        while True:
            usuario = input("Usuario: ").lower()
            contra = input("Constraseña: ")
            if usuario and contra in alumnos.csv or admin.csv:
                return usuario, contra
            else:
                print("Error, Usuario o Contraseña incorrectas.")

    def _tratar_opcion(self, usuario: str, contra: str):
        while True:
            match usuario and contra:
                case usuario, contra in alumnos.csv:
                    Menuusuario()
                case usuario, contra in admins.csv:
                    Menuadmin()
                case _:
                    print("Error")

    def _login(self):
        self._imprimir_menu()
        self._recoger_opcion()
        self._tratar_opcion()
