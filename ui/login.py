import csv
from typing import Tuple
from ui.menu_admin import Menuadmin

class Login:

    ESPACIOS: int = 60

    def _imprimir_menu(self):
        print("-" * self.ESPACIOS)
        print("INICIO DE SESION DE USUARIOS".center(self.ESPACIOS))
        print("-" * self.ESPACIOS)

    @staticmethod
    def _recoger_usuario_contra() -> Tuple[str, str]:
            usuario = input("Usuario: ").lower()
            contra = input("Constraseña: ")
            return usuario, contra

    @staticmethod
    def _verificar_credenciales( usuario: str, contra: str, archivo: str) -> bool:
        try:
            with open(archivo, newline='', encoding='utf-8') as csvfile:
                lector = csv.reader(csvfile)
                for fila in lector:
                    if len(fila) >= 2 and fila[0] == usuario and fila[1] == contra:
                        return True
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
        return False

    def _tratar_opcion(self, usuario: str, contra: str):
        if self._verificar_credenciales(usuario, contra, "admins.csv"):
            Menuadmin()
        else:
            print("Usuario o Contraseña Incorrectos.")

    def _login(self):
        self._imprimir_menu()
        usuario, contra = self._recoger_usuario_contra()
        self._tratar_opcion(usuario, contra)