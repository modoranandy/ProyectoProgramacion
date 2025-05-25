import unittest
from lib.Cursos import Curso
from config.config import NivelCurso

class TestCurso(unittest.TestCase):
    def test_init(self):
        curso = Curso(1, NivelCurso.PRIMARIA, "A")
        self.assertEqual(curso.curso, 1)
        self.assertEqual(curso.nivel, NivelCurso.PRIMARIA)
        self.assertEqual(curso.letra, "A")

        curso = Curso()
        self.assertEqual(curso.curso, 0)
        self.assertEqual(curso.nivel, NivelCurso.SECUNDARIA)
        self.assertEqual(curso.letra, "A")

        curso = Curso(letra="b")
        self.assertEqual(curso.letra, "B")

        curso = Curso(nivel=None)
        self.assertEqual(curso.nivel, NivelCurso.SECUNDARIA)

    def test_str(self):
        curso = Curso(2, NivelCurso.BACHILLERATO, "C")
        self.assertEqual(str(curso), "2 BACHILLERATO C")

    def test_eq(self):
        curso1 = Curso(3, NivelCurso.SECUNDARIA, "D")
        curso2 = Curso(3, NivelCurso.SECUNDARIA, "D")
        curso3 = Curso(4, NivelCurso.SECUNDARIA, "D")
        curso4 = Curso(3, NivelCurso.BACHILLERATO, "D")
        curso5 = Curso(3, NivelCurso.SECUNDARIA, "E")

        self.assertEqual(curso1, curso2)
        self.assertNotEqual(curso1, curso3)
        self.assertNotEqual(curso1, curso4)
        self.assertNotEqual(curso1, curso5)

if __name__ == "__main__":
    unittest.main()
