from Cursos import Curso
curso = Curso
class Alumno:

    def __init__(self, nombre:str, apellido:str, edad:int, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.curso}"