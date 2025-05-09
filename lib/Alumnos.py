from Cursos import Curso

class Alumno:

    def __init__(self, nombre:str = "Alumno", apellido:str = "0", edad:int = "0", curso: Curso | None = None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso if curso in Curso else Curso()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.curso}"

    def __eq__(self, other):
        if isinstance(other, Alumno):
            return self.nombre == other.nombre and self.apellido == other.apellido and self.edad == other.edad
        else:
            return False