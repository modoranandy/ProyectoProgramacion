from config.config import EstadoLibro

class Libro:
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
        estado = EstadoLibro(int(input("Estado : ")))
        return Libro(titulo, autor, numero_ejemplares, isbn, estado)