import csv
from config.config import EstadoPrestamo

RUTA_CSV = "config/prestamos.csv"


class Prestamo:
    CAMPOS = [ "isbn", "dni_alumno", "fecha_prestamo", "fecha_devolucion", "estado"]

    def __init__(self, isbn:str = "00000000X", dni_alumno:str = "0000000X", fecha_prestamo:str = "00/00/0000",
                 fecha_devolucion:str = "00/00/0000", estado :EstadoPrestamo | None = None):
        self.isbn:str = str(isbn)
        self.dni_alumno:str = str(dni_alumno)
        self.fecha_prestamo:str = str(fecha_prestamo)
        self.fecha_devolucion:str = str(fecha_devolucion)
        self.estado: EstadoPrestamo = estado if estado in EstadoPrestamo else EstadoPrestamo.NOPRESTADO

    def __str__(self):
        return (f"Préstamo:\n Libro: {self.isbn} a {self.dni_alumno} "
                f"({self.fecha_prestamo} - {self.fecha_devolucion}) Estado: {self.estado}")

    def __eq__(self, other):
        if isinstance(other, Prestamo):
            return self.isbn == other.isbn
        return False

    @staticmethod
    def add_new_prestamo():
        isbn = input("ISBN del libro: ")
        dni_alumno = input("DNI/NIE del alumno: ")
        fecha_prestamo = input("Fecha de préstamo (DD/MM/YYYY): ")
        fecha_devolucion = input("Fecha de devolución (DD/MM/YYYY): ")
        for p in EstadoPrestamo:
            print(f"{p.value}:{p.name}")
        estado = EstadoPrestamo(input("Estado del prestamo: "))
        return Prestamo(isbn, dni_alumno, fecha_prestamo, fecha_devolucion, estado)

    @staticmethod
    def buscar_prestamo_por_isbn(prestamos, isbn):
        for prestamo in prestamos:
            if prestamo.isbn == isbn:
                return prestamo
        return None

    @staticmethod
    def eliminar_prestamo(prestamos, isbn):
        prestamo = Prestamo.buscar_prestamo_por_isbn(prestamos, isbn)
        if prestamo:
            prestamos.remove(prestamo)
            Prestamo.guardar_prestamos(prestamos)
            print("Préstamo eliminado correctamente.")
            return True
        else:
            print("No se ha encontrado ningún préstamo con ese ISBN.")
            return False

    @staticmethod
    def cargar_prestamos():
        prestamos = []
        try:
            with open(RUTA_CSV, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for i, fila in enumerate(reader):
                    if not fila or len(fila) < 5:
                        continue
                    if i == 0 and fila[4].lower() == "estado":
                        continue
                    try:
                        prestamos.append(Prestamo(
                            isbn=fila[0],
                            dni_alumno=fila[1],
                            fecha_prestamo=fila[2],
                            fecha_devolucion=fila[3],
                            estado=EstadoPrestamo(int(fila[4]))
                        ))
                    except Exception as e:
                        print(f"Error en la fila {i + 1}: {fila}. Detalle: {e}")
        except FileNotFoundError:
            pass
        return prestamos

    @staticmethod
    def guardar_prestamos(prestamos):
        with open(RUTA_CSV, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(Prestamo.CAMPOS)
            for prestamo in prestamos:
                writer.writerow([
                    prestamo.isbn,
                    prestamo.dni_alumno,
                    prestamo.fecha_prestamo,
                    prestamo.fecha_devolucion,
                    prestamo.estado.value
                ])

def editar_prestamo(prestamos):
    isbn = input("Introduce el ISBN del préstamo que deseas editar: ")
    prestamo = None
    for p in prestamos:
        if p.isbn == isbn:
            prestamo = p
            break
    if not prestamo:
        print("No se ha encontrado ningún préstamo con ese ISBN.")
        return

    print(f"\nEditando préstamo: {prestamo}")

    nuevo_isbn = input(f"ISBN [{prestamo.isbn}]: ")
    nuevo_dni = input(f"DNI/NIE [{prestamo.dni_alumno}]: ")
    nueva_fecha_prestamo = input(f"Fecha de préstamo [{prestamo.fecha_prestamo}]: ")
    nueva_fecha_devolucion = input(f"Fecha de devolución [{prestamo.fecha_devolucion}]: ")
    nuevo_estado = int(input(f"Estado (0=ACTIVO, 1=FINALIZADO) [{prestamo.estado}]: "))

    if nuevo_isbn:
        prestamo.isbn = nuevo_isbn
    if nuevo_dni:
        prestamo.dni_alumno = nuevo_dni
    if nueva_fecha_prestamo:
        prestamo.fecha_prestamo = nueva_fecha_prestamo
    if nueva_fecha_devolucion:
        prestamo.fecha_devolucion = nueva_fecha_devolucion
    if nuevo_estado and nuevo_estado in ("0", "1"):
        prestamo.estado = int(nuevo_estado)

    print("Préstamo editado correctamente.")
    Prestamo.guardar_prestamos(prestamos)