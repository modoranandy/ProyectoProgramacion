from enum import Enum

class EstadoLibro(Enum):
    ENLABIBLIOTECA = 0
    PRESTADO = 1
    DEVUELTO = 2


def get_all_values_enum(enumeracion: any) -> [int]:
    return [e.value for e in enumeracion]

def make_enum_to_str(enumeracion):
    return str({e.value: e.name for e in enumeracion})