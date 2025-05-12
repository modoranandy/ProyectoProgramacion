from abc import abstractmethod

class Menu:

    @abstractmethod
    def main(self):
        self.visualizar_menu()
        self.recoger_menu_opcion()

    @abstractmethod
    def visualizar_menu(self):
        print("-" * 60 + "\n",
              " " * 20 + "Menú Principal" + "\n",
              "-" * 60 + "\n",
              "1.- Añadir un nuevo parque \n"
              "2.- Borrar parque \n"
              "3.- Ver todos los parques \n"
              "4.- Hacer parque activo \n"
              "5.- Ver parque activo \n"
              "6.- Ir al parque activo \n"
              "7.- Salir \n",
              "-" * 60 + "\n")

    @abstractmethod
    def recoger_menu_opcion(self):
        opcion:int = int(input("¿Opcion?> "))
        return opcion

    @abstractmethod
    def tratar_opcion_menu(self, opcion):
        match opcion:
            case 1:
                self.opcion1()
            case 2:
                self.opcion2()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case _:
                print("Opcion invalida, introduzca de nuevo una opcion valida porfavor.")

    @staticmethod
    def opcion1() -> str and int:
        print("-" * 60 + "\n",
              "¿Opción?>1\n",
              "-" * 60 + "\n",
              " " * 20 + "Datos para nuevo parque:" + "\n",
              "-" * 60 + "\n")
        nombre = input("¿Nombre?> ")
        tipo:int = int(input("¿Tipo[{0: 'FLUVIAL', 1: 'COSTERO', 2: 'INTERIOR'}]?> "))
        return nombre, tipo

    @staticmethod
    def opcion2() -> str:
        print("-" * 60 + "\n",
              "¿Opción?>2\n",
              "-" * 60 + "\n",
              " " * 20 + "Parques Actuales:" + "\n",
              "-" * 60 + "\n")
        # Llamada a mostrar parques y que muestre todos los parques que hay FUNCION
        nombre = input("¿Nombre del parque a borrar?> ")
        return nombre

    @staticmethod
    def opcion3() -> None:
        print("-" * 60 + "\n",
              "¿Opcion?>3\n",
              "-" * 60 + "\n",
              " " * 20 + "Parques Actuales:" + "\n",
              "-" * 60 + "\n")
        # For parque en lista parques: print parques FUNCION

    @staticmethod
    def opcion4() -> str:
        print("-" * 60 + "\n",
              "¿Opción?>4\n",
              "-" * 60 + "\n",
        # for nombre in parques_activos: print f"Parque Actual: {nombre}" Separarlo EN UNA FUNCION
              "-" * 60 + "\n")
        # For parque en lista parques: print parques FUNCION
        print("-" * 60 + "\n")
        nombre = input("¿Nombre del parque a activar?> ")
        return nombre

    @staticmethod
    def opcion5() -> str:
        pass