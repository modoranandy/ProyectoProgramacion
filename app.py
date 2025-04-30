from ui.login import Login




class App:

    def run(self):

        self.libros = {}
        self.alumnos = {}
        self.administradores = {}

        aux:bool = True

        while aux:

            login = Login()
            login.imprimir_menu()
            opcion = input("Introduzca la opcion: ").upper()

            match opcion:

                case "S":
                    pass

                case "N":
                    pass

                case _:
                    raise ValueError("Opcion invalida")

    def menu_usuario(self):
        pass

    def menu_administrador(self):
        pass