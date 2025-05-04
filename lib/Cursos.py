class Curso:
    def __init__(self, curso:int, nivel:str, letra:str):
        self.curso = curso
        self.nivel = nivel
        self.letra = letra

    def __str__(self):
        return f"{self.curso} {self.nivel} {self.letra}"