import csv
from config.config import EstadoLibro

RUTA_CSV = "config/libros.csv"

class Libro:

    CAMPOS = ["titulo" "autor" "numero_ejemplares" "isbn" "estado"]

    def __init__(self, titulo:str ="Titulo", autor:str = "Autor" , numero_ejemplares:int = 0,
                 isbn:str ="0000000X" , estado: EstadoLibro | None = None ):
        self.titulo:str = str(titulo)
        self.autor:str = str(autor)
        self.numero_ejemplares:int = int(numero_ejemplares)
        self.isbn:str = str(isbn)
        self.estado = estado if estado in EstadoLibro else EstadoLibro.ENLABIBLIOTECA

    def __str__(self):
        return (f"{self.titulo} {self.autor} {self.numero_ejemplares} {self.isbn} "
                f" {self.estado}")

    def __eq__(self, other):
        if isinstance(other, Libro):
            return self.isbn == other.isbn
        return False

    @staticmethod
    def add_new_libro():
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        numero_ejemplares = int(input("Número de ejemplares: "))
        isbn = input("ISBN: ")
        print("Opciones de Estado:")
        for e in EstadoLibro:
            print(f"{e.value}: {e.name}")
        estado = EstadoLibro(int(input("Estado: ")))
        return Libro(titulo, autor, numero_ejemplares, isbn, estado)

    @staticmethod
    def buscar_libro_por_isbn(libros, isbn):
        for libro in libros:
            if libro.isbn == isbn:
                return libro
        return None

    @staticmethod
    def eliminar_libro(libros, isbn):
        libro = Libro.buscar_libro_por_isbn(libros, isbn)
        if libro:
            libros.remove(libro)
            Libro.guardar_libros(libros)
            print("Libro eliminado correctamente.")
            return True
        else:
            print("No se ha encontrado ningún libro con ese ISBN.")
            return False

    @staticmethod
    def cargar_libros():
        libros = []
        try:
            with open(RUTA_CSV, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for fila in reader:
                    if fila:
                        libros.append(Libro(
                            titulo=fila[0],
                            autor=fila[1],
                            numero_ejemplares=int(fila[2]),
                            isbn=fila[3],
                            estado=EstadoLibro(int(fila[4]))
                        ))
        except FileNotFoundError:
            pass
        return libros

    @staticmethod
    def guardar_libros(libros):
        with open(RUTA_CSV, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(Libro.CAMPOS)
            for libro in libros:
                writer.writerow([
                    libro.titulo,
                    libro.autor,
                    libro.numero_ejemplares,
                    libro.isbn,
                    libro.estado.value
                ])

def editar_libro(libros):
    isbn = input("Introduce el ISBN del libro que deseas editar: ")
    libro = None
    for l in libros:
        if l.isbn == isbn:
            libro = l
            break
    if not libro:
        print("No se ha encontrado ningún libro con ese ISBN.")
        return

    print(f"\nEditando libro: {libro.titulo} ({libro.isbn})")

    nuevo_titulo = input(f"Título [{libro.titulo}]: ")
    nuevo_autor = input(f"Autor [{libro.autor}]: ")
    nuevo_numero_ejemplares = input(f"Número de ejemplares [{libro.numero_ejemplares}]: ")

    print("Opciones de Estado:")
    for e in EstadoLibro:
        print(f"{e.value}: {e.name}")
    nuevo_estado = input(f"Estado [{libro.estado.value}]: ")

    if nuevo_titulo:
        libro.titulo = nuevo_titulo
    if nuevo_autor:
        libro.autor = nuevo_autor
    if nuevo_numero_ejemplares:
        libro.numero_ejemplares = int(nuevo_numero_ejemplares)
    if nuevo_estado:
        libro.estado = EstadoLibro(int(nuevo_estado))

    print("Libro editado correctamente.")
    Libro.guardar_libros(libros)