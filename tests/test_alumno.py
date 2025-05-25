import unittest
import os
import csv
from lib.Alumnos import Alumno
from lib.Cursos import Curso
from config.config import NivelCurso, Tramos, Bilingue

class TestAlumno(unittest.TestCase):
    def setUp(self):
        # Crear archivo CSV de prueba (en la misma carpeta de tests)
        self.test_csv = "test_alumnos.csv"
        with open(self.test_csv, "w", newline='', encoding='utf-8') as f:
            f.write("dni,nombre,apellido,edad,tramo,bilingue,curso,nivel,letra\n")
            f.write("12345678A,Juan,Perez,14,1,1,1,1,A\n")
        # Guardar la ruta original
        self.original_path = Alumno.RUTA_CSV
        # Cambiar la ruta al archivo de prueba
        Alumno.RUTA_CSV = self.test_csv

    def tearDown(self):
        # Restaurar la ruta original
        Alumno.RUTA_CSV = self.original_path
        # Borrar el archivo de prueba si existe
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_cargar_alumnos(self):
        alumnos = Alumno.cargar_alumnos()
        self.assertEqual(len(alumnos), 1)
        self.assertEqual(alumnos[0].nombre, "JUAN")
        self.assertEqual(alumnos[0].dni, "12345678A")
        self.assertEqual(alumnos[0].edad, 14)

    def test_guardar_alumnos(self):
        # Crear un alumno de prueba
        curso = Curso(2, NivelCurso(2), "B")
        alumno = Alumno("Ana", "Garcia", 15, Tramos(2), "23456789B", curso, Bilingue(0))
        # Guardar
        Alumno.guardar_alumnos([alumno])
        # Leer y comprobar
        with open(self.test_csv, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            lineas = [fila for fila in reader]
        # Cabecera + 1 alumno
        self.assertEqual(len(lineas), 2)
        # Comprobar que el alumno está guardado
        self.assertEqual(lineas[1][0], "23456789B")
        self.assertEqual(lineas[1][1], "ANA")
        self.assertEqual(lineas[1][2], "GARCIA")

if __name__ == "__main__":
    unittest.main()