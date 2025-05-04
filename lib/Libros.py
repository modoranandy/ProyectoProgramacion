class Libro:
    def __init__(self, titulo:str , autor:str , numero_ejemplares:int, isbn:int, fecha_entrega:int, fecha_devolucion:int, estado:str):
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares
        self.isbn = isbn
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def __str__(self):
        return f"{self.titulo} {self.autor} {self.numero_ejemplares} {self.isbn} {self.fecha_entrega} {self.fecha_devolucion} {self.estado}"