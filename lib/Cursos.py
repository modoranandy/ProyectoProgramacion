from config.config import NivelCurso

class Curso:
    def __init__(self, curso:int = 0, nivel: NivelCurso | None = None, letra:str = "A"):
        self.curso:int = int(curso)
        self.nivel: NivelCurso = nivel if nivel in NivelCurso else NivelCurso.SECUNDARIA
        self.letra:str = str(letra)

    def __str__(self):
        return f"{self.curso} {self.nivel} {self.letra}"

    def __eq__(self, other):
        if isinstance(other, Curso):
            return self.curso == other.curso and self.nivel == other.nivel and self.letra == other.letra
        return False