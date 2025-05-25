import unittest
import os
import csv
from lib.Prestamos import Prestamo
from config.config import EstadoPrestamo

class TestPrestamo(unittest.TestCase):
    def setUp(self):
        self.test_csv = "test_prestamos.csv"
        with open(self.test_csv, "w", newline='', encoding='utf-8') as f:
            f.write("isbn,dni_alumno,fecha_prestamo,fecha_devolucion,estado\n")
            f.write("1234567890,12345678A,2025-05-20,2025-06-03,0\n")
        self.original_path = Prestamo.RUTA_CSV
        Prestamo.RUTA_CSV = self.test_csv

    def tearDown(self):
        Prestamo.RUTA_CSV = self.original_path
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_init(self):
        prestamo = Prestamo("1111111111", "23456789B", "2025-05-22", "2025-06-04", EstadoPrestamo(0))
        self.assertEqual(prestamo.isbn, "1111111111")
        self.assertEqual(prestamo.dni_alumno, "23456789B")
        self.assertEqual(prestamo.fecha_prestamo, "2025-05-22")
        self.assertEqual(prestamo.fecha_devolucion, "2025-06-04")
        self.assertEqual(prestamo.estado, EstadoPrestamo(0))

        prestamo = Prestamo()
        self.assertEqual(prestamo.isbn, "00000000X")
        self.assertEqual(prestamo.dni_alumno, "0000000X")
        self.assertEqual(prestamo.fecha_prestamo, "00/00/0000")
        self.assertEqual(prestamo.fecha_devolucion, "00/00/0000")
        self.assertEqual(prestamo.estado, EstadoPrestamo.NOPRESTADO)

    def test_str(self):
        prestamo = Prestamo("2222222222", "34567890C", "2025-05-23", "2025-06-05", EstadoPrestamo(1))
        self.assertIn("2222222222", str(prestamo))
        self.assertIn("34567890C", str(prestamo))
        self.assertIn("2025-05-23", str(prestamo))
        self.assertIn("2025-06-05", str(prestamo))
        self.assertIn("Estado:", str(prestamo))

    def test_eq(self):
        prestamo1 = Prestamo("3333333333", "45678901D", "2025-05-24", "2025-06-06", EstadoPrestamo(0))
        prestamo2 = Prestamo("3333333333", "45678901D", "2025-05-24", "2025-06-06", EstadoPrestamo(0))
        prestamo3 = Prestamo("4444444444", "45678901D", "2025-05-24", "2025-06-06", EstadoPrestamo(0))
        self.assertEqual(prestamo1, prestamo2)
        self.assertNotEqual(prestamo1, prestamo3)

    def test_cargar_prestamos(self):
        prestamos = Prestamo.cargar_prestamos()
        self.assertEqual(len(prestamos), 1)
        self.assertEqual(prestamos[0].isbn, "1234567890")
        self.assertEqual(prestamos[0].dni_alumno, "12345678A")
        self.assertEqual(prestamos[0].fecha_prestamo, "2025-05-20")
        self.assertEqual(prestamos[0].fecha_devolucion, "2025-06-03")
        self.assertEqual(prestamos[0].estado, EstadoPrestamo(0))

    def test_guardar_prestamos(self):
        prestamo = Prestamo("5555555555", "56789012E", "2025-05-25", "2025-06-07", EstadoPrestamo(1))
        Prestamo.guardar_prestamos([prestamo])
        with open(self.test_csv, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            lineas = [fila for fila in reader]
        self.assertEqual(len(lineas), 2)
        self.assertEqual(lineas[1][0], "5555555555")
        self.assertEqual(lineas[1][1], "56789012E")
        self.assertEqual(lineas[1][2], "2025-05-25")
        self.assertEqual(lineas[1][3], "2025-06-07")
        self.assertEqual(lineas[1][4], "1")

    def test_buscar_prestamo_por_isbn(self):
        prestamos = [
            Prestamo("6666666666", "67890123F", "2025-05-26", "2025-06-08", EstadoPrestamo(0)),
            Prestamo("7777777777", "78901234G", "2025-05-27", "2025-06-09", EstadoPrestamo(1))
        ]
        encontrado = Prestamo.buscar_prestamo_por_isbn(prestamos, "6666666666")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.isbn, "6666666666")
        no_encontrado = Prestamo.buscar_prestamo_por_isbn(prestamos, "9999999999")
        self.assertIsNone(no_encontrado)

if __name__ == "__main__":
    unittest.main()
