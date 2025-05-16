from Cursos import Curso
from config.config import NivelCurso


class Alumno:

    def __init__(self, nombre:str = "Alumno", apellido:str = "0", edad:int = 0,
                 dni:str = "000000000X",curso: Curso | None = None):
        self.nombre:str = str(nombre).upper()
        self.apellido:str = str(apellido).upper()
        self.edad:int = int(edad)
        self.dni:str = str(dni).upper()
        self.curso: Curso = curso if isinstance(curso,Curso) else Curso()

    def __str__(self):
        return (f"Alumno: {self.nombre},{self.apellido}, con DNI/NIE {self.dni} de {self.edad} "
                f"años, esta cursando {self.curso} ")

    def __eq__(self, other):
        if isinstance(other, Alumno):
            return self.dni == other.dni
        return False

    @staticmethod
    def _add_new_alumno():
        nombre = input("Nombre del Alumno: ")
        apellido = input("Apellido del Alumno: ")
        edad = int(input("Edad del Alumno: "))
        dni = input("DNI/NIE del Alumno: ")
        curso = int(input("Curso del Alumno: "))
        nivel = int(input("Nivel del Alumno: "))
        letra = str(input("Letra del Alumno: "))
        curso = Curso(curso,NivelCurso(nivel),letra)
        nuevo_alumno = Alumno(nombre, apellido, edad, dni, curso)
        return nuevo_alumno

    @staticmethod
    def _del_alumno():
        nombre = input("Nombre del Alumno a eliminar: ")
        if nombre in Alumno: #En el csv:
            del Alumno