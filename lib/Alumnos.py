from Cursos import Curso

class Alumno:

    def __init__(self, nombre:str = "Alumno", apellido:str = "0", edad:int = 0, curso: Curso | None = None):
        self.nombre:str = str(nombre)
        self.apellido:str = str(apellido)
        self.edad:int = int(edad)
        self.curso: Curso = curso if isinstance(curso,Curso) else Curso()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.curso}"

    def __eq__(self, other):
        if isinstance(other, Alumno):
            return self.nombre == other.nombre and self.apellido == other.apellido and self.edad == other.edad
        return False