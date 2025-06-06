from enum import Enum

class EstadoLibro(Enum):
    ENLABIBLIOTECA = 0
    PRESTADO = 1
    DEVUELTO = 2

class NivelCurso(Enum):
    INFANTIL = 0
    PRIMARIA = 1
    SECUNDARIA = 2
    BACHILLERATO = 3
    GRADO = 4

class Tramos(Enum):
    I = 0
    II = 1
    NINGUNO = 2

class Bilingue(Enum):
    NO = 0
    SI = 1

class EstadoPrestamo(Enum):
    NOPRESTADO = 0
    PRESTADO = 1

def get_all_values_enum(enumeracion: any) -> [int]:
    return [e.value for e in enumeracion]

def make_enum_to_str(enumeracion):
    return str({e.value: e.name for e in enumeracion})