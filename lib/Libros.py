from config import EstadoLibro

class Libro:
    def __init__(self, titulo:str ="Titulo", autor:str = "Autor" , numero_ejemplares:int = 0,
                 isbn:str ="0000000X" , fecha_entrega:str = "00/00/0000",
                 fecha_devolucion:str = "00/00/0000", estado: EstadoLibro | None = None ):
        self.titulo:str = str(titulo)
        self.autor:str = str(autor)
        self.numero_ejemplares:int = int(numero_ejemplares)
        self.isbn:int = int(isbn)
        self.fecha_entrega:str = str(fecha_entrega)
        self.fecha_devolucion:str = str(fecha_devolucion)
        self.estado = estado if estado in EstadoLibro else EstadoLibro.ENLABIBLIOTECA

    def __str__(self):
        return (f"{self.titulo} {self.autor} {self.numero_ejemplares} {self.isbn} "
                f"{self.fecha_entrega} {self.fecha_devolucion} {self.estado}")

    def __eq__(self, other):
        if isinstance(other, Libro):
            return self.isbn == other.isbn
        else:
            return False