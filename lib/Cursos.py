class Curso:
    def __init__(self, curso:int = 0, nivel:str = "Infantil", letra:str = "A"):
        self.curso:int = int(curso)
        self.nivel:str = str(nivel)
        self.letra:str = str(letra)

    def __str__(self):
        return f"{self.curso} {self.nivel} {self.letra}"

    def __eq__(self, other):
        if isinstance(other, Curso):
            return self.curso == other.curso and self.nivel == other.nivel and self.letra == other.letra
        return False

