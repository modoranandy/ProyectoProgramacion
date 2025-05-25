import unittest
import os
import csv
from lib.Admins import Admin

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.test_csv = "test_admins.csv"
        with open(self.test_csv, "w", newline='', encoding='utf-8') as f:
            f.write("nombre,apellido,edad\n")
            f.write("Maria,Garcia,35\n")
        self.original_path = Admin.RUTA_CSV
        Admin.RUTA_CSV = self.test_csv

    def tearDown(self):
        Admin.RUTA_CSV = self.original_path
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_cargar_admins(self):
        admins = Admin.cargar_admins()
        self.assertEqual(len(admins), 1)
        self.assertEqual(admins[0].nombre, "Maria")
        self.assertEqual(admins[0].apellido, "Garcia")
        self.assertEqual(admins[0].edad, 35)

    def test_guardar_admins(self):
        admin = Admin("Juan", "Perez", 40)
        Admin.guardar_admins([admin])
        with open(self.test_csv, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            lineas = [fila for fila in reader]
        self.assertEqual(len(lineas), 2)
        self.assertEqual(lineas[1][0], "Juan")
        self.assertEqual(lineas[1][1], "Perez")
        self.assertEqual(lineas[1][2], "40")

if __name__ == "__main__":
    unittest.main()
