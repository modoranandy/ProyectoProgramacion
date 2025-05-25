import csv
from lib.Alumnos import Alumno, editar_alumno
from lib.Libros import Libro, editar_libro
from lib.Prestamos import Prestamo, editar_prestamo



class Admin:

    CAMPOS = ["nombre", "apellido", "edad"]
    RUTA_CSV = "config/admins.csv"

    def __init__(self, nombre: str = "Admin", apellido: str = "0", edad: int = 0):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.edad = int(edad)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"

    def __eq__(self, other):
        if isinstance(other, Admin):
            return self.nombre == other.nombre and self.apellido == other.apellido
        return False

    @staticmethod
    def _add_new_admin():
        nombre = input("Nombre del admin: ")
        apellido = input("Apellido del admin: ")
        edad = int(input("Edad del admin: "))
        return Admin(nombre, apellido, edad)

    @staticmethod
    def cargar_admins():
        admins = []
        try:
            with open(Admin.RUTA_CSV, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                for fila in reader:
                    if fila:
                        admins.append(Admin(
                            nombre=fila[0],
                            apellido=fila[1],
                            edad=int(fila[2])
                        ))
        except FileNotFoundError:
            pass
        return admins

    @staticmethod
    def guardar_admins(admins):
        with open(Admin.RUTA_CSV, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(Admin.CAMPOS)
            for admin in admins:
                writer.writerow([
                    admin.nombre,
                    admin.apellido,
                    admin.edad
                ])
    @staticmethod
    def mostrar_libros():
        libros = Libro.cargar_libros()
        for libro in libros:
            print(libro)

    @staticmethod
    def anadir_libro():
        libros = Libro.cargar_libros()
        nuevo = Libro.add_new_libro()
        if Libro.buscar_libro_por_isbn(libros, nuevo.isbn):
            print("Ya existe un libro con ese ISBN.")
            return
        libros.append(nuevo)
        Libro.guardar_libros(libros)
        print("Libro añadido correctamente.")

    @staticmethod
    def eliminar_libro():
        libros = Libro.cargar_libros()
        isbn = input("Introduce el ISBN del libro a eliminar: ")
        Libro.eliminar_libro(libros, isbn)

    @staticmethod
    def modificar_libro():
        libros = Libro.cargar_libros()
        editar_libro(libros)

    @staticmethod
    def mostrar_prestamos():
        prestamos = Prestamo.cargar_prestamos()
        for prestamo in prestamos:
            print(prestamo)

    @staticmethod
    def anadir_prestamo():
        prestamos = Prestamo.cargar_prestamos()
        nuevo = Prestamo.add_new_prestamo()
        if Prestamo.buscar_prestamo_por_isbn(prestamos, nuevo.isbn):
            print("Ya existe un préstamo activo para ese libro.")
            return
        prestamos.append(nuevo)
        Prestamo.guardar_prestamos(prestamos)
        print("Préstamo añadido correctamente.")

    @staticmethod
    def eliminar_prestamo():
        prestamos = Prestamo.cargar_prestamos()
        isbn = input("Introduce el ISBN del préstamo a eliminar: ")
        Prestamo.eliminar_prestamo(prestamos, isbn)

    @staticmethod
    def modificar_prestamo():
        prestamos = Prestamo.cargar_prestamos()
        editar_prestamo(prestamos)

    @staticmethod
    def mostrar_alumnos():
        alumnos = Alumno.cargar_alumnos()
        for alumno in alumnos:
            print(alumno)

    @staticmethod
    def anadir_alumno():
        alumnos = Alumno.cargar_alumnos()
        nuevo = Alumno.add_new_alumno()
        if Alumno.buscar_alumno_por_dni(alumnos, nuevo.dni):
            print("Ya existe un alumno con ese DNI/NIE.")
            return
        alumnos.append(nuevo)
        Alumno.guardar_alumnos(alumnos)
        print("Alumno añadido correctamente.")

    @staticmethod
    def eliminar_alumno():
        alumnos = Alumno.cargar_alumnos()
        dni = input("Introduce el DNI/NIE del alumno a eliminar: ")
        Alumno.eliminar_alumno(alumnos, dni)

    @staticmethod
    def modificar_alumno():
        alumnos = Alumno.cargar_alumnos()
        editar_alumno(alumnos)

    @staticmethod
    def mostrar_cursos():
        alumnos = Alumno.cargar_alumnos()
        for alumno in alumnos:
            print(f"Alumno: {alumno.dni}, Curso: {alumno.curso}")