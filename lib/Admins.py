import csv

RUTA_CSV = "config/admins.csv"

class Admin:

    CAMPOS = "nombre" "apellido" "edad"

    def __init__(self, nombre:str = "Admin", apellido:str = "0", edad:int = 0):
        self.nombre:str = str(nombre)
        self.apellido:str = str(apellido)
        self.edad:int = int(edad)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"

    def __eq__(self, other):
        if isinstance(other, Admin):
            return self.nombre == other.nombre
        return False