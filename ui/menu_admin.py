from lib.Admins import Admin
from config.backup import copia_seguridad
from config.vaciar_csvs import vaciar_todos_los_csv
from config.carga_inicial import carga_inicial

class MenuAdmin:
    def __init__(self):
        self.admin = Admin()

    def main(self):
        while True:
            print("\n--- MENÚ PRINCIPAL DE ADMINISTRACIÓN ---")
            print("1. Gestionar Libros")
            print("2. Gestionar Alumnos")
            print("3. Gestionar Préstamos")
            print("4. Modificar Curso de Alumno")
            print("5. Copia de seguridad de datos")
            print("6. Vaciar todos los datos (Reset)")
            print("7. Carga inicial de datos")
            print("8. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self._mostrar_menu_libros()
            elif opcion == "2":
                self._mostrar_menu_alumnos()
            elif opcion == "3":
                self._mostrar_menu_prestamos()
            elif opcion == "4":
                self.admin.modificar_alumno()
            elif opcion == "5":
                copia_seguridad()
            elif opcion == "6":
                vaciar_todos_los_csv()
            elif opcion == "7":
                carga_inicial()
            elif opcion == "8":
                print("Cerrando sesión de administrador...")
                break
            else:
                print("Opción no válida.")

    def _mostrar_menu_libros(self):
        print("\n--- GESTIÓN DE LIBROS ---")
        print("1. Mostrar libros")
        print("2. Añadir libro")
        print("3. Eliminar libro")
        print("4. Modificar libro")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.admin.mostrar_libros()
        elif opcion == "2":
            self.admin.anadir_libro()
        elif opcion == "3":
            self.admin.eliminar_libro()
        elif opcion == "4":
            self.admin.modificar_libro()
        else:
            print("Opción no válida. Volviendo al menú principal.")

    def _mostrar_menu_alumnos(self):
        print("\n--- GESTIÓN DE ALUMNOS ---")
        print("1. Mostrar alumnos")
        print("2. Añadir alumno")
        print("3. Eliminar alumno")
        print("4. Modificar alumno")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.admin.mostrar_alumnos()
        elif opcion == "2":
            self.admin.anadir_alumno()
        elif opcion == "3":
            self.admin.eliminar_alumno()
        elif opcion == "4":
            self.admin.modificar_alumno()
        else:
            print("Opción no válida. Volviendo al menú principal.")

    def _mostrar_menu_prestamos(self):
        print("\n--- GESTIÓN DE PRÉSTAMOS ---")
        print("1. Mostrar préstamos")
        print("2. Añadir préstamo")
        print("3. Eliminar préstamo")
        print("4. Modificar préstamo")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.admin.mostrar_prestamos()
        elif opcion == "2":
            self.admin.anadir_prestamo()
        elif opcion == "3":
            self.admin.eliminar_prestamo()
        elif opcion == "4":
            self.admin.modificar_prestamo()
        else:
            print("Opción no válida. Volviendo al menú principal.")