import unittest
import os
import csv
from lib.Libros import Libro
from config.config import EstadoLibro

class TestLibro(unittest.TestCase):
    def setUp(self):
        self.test_csv = "test_libros.csv"
        with open(self.test_csv, "w", newline='', encoding='utf-8') as f:
            f.write("titulo,autor,numero_ejemplares,isbn,estado\n")
            f.write("El Quijote,Miguel de Cervantes,5,1234567890,0\n")
        self.original_path = Libro.RUTA_CSV
        Libro.RUTA_CSV = self.test_csv

    def tearDown(self):
        Libro.RUTA_CSV = self.original_path
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_init(self):
        libro = Libro("Cien años de soledad", "Gabriel García Márquez", 3, "0987654321", EstadoLibro(0))
        self.assertEqual(libro.titulo, "Cien años de soledad")
        self.assertEqual(libro.autor, "Gabriel García Márquez")
        self.assertEqual(libro.numero_ejemplares, 3)
        self.assertEqual(libro.isbn, "0987654321")
        self.assertEqual(libro.estado, EstadoLibro(0))

        libro = Libro()
        self.assertEqual(libro.titulo, "Titulo")
        self.assertEqual(libro.autor, "Autor")
        self.assertEqual(libro.numero_ejemplares, 0)
        self.assertEqual(libro.isbn, "0000000X")
        self.assertEqual(libro.estado, EstadoLibro.ENLABIBLIOTECA)

    def test_str(self):
        libro = Libro("El Principito", "Antoine de Saint-Exupéry", 2, "1234567890", EstadoLibro(1))
        self.assertIn("El Principito", str(libro))
        self.assertIn("Antoine de Saint-Exupéry", str(libro))
        self.assertIn("1234567890", str(libro))

    def test_eq(self):
        libro1 = Libro("El Hobbit", "J.R.R. Tolkien", 4, "1111111111", EstadoLibro(0))
        libro2 = Libro("El Hobbit", "J.R.R. Tolkien", 4, "1111111111", EstadoLibro(0))
        libro3 = Libro("El Hobbit", "J.R.R. Tolkien", 4, "2222222222", EstadoLibro(0))
        self.assertEqual(libro1, libro2)
        self.assertNotEqual(libro1, libro3)

    def test_cargar_libros(self):
        libros = Libro.cargar_libros()
        self.assertEqual(len(libros), 1)
        self.assertEqual(libros[0].titulo, "El Quijote")
        self.assertEqual(libros[0].autor, "Miguel de Cervantes")
        self.assertEqual(libros[0].numero_ejemplares, 5)
        self.assertEqual(libros[0].isbn, "1234567890")
        self.assertEqual(libros[0].estado, EstadoLibro(0))

    def test_guardar_libros(self):
        libro = Libro("1984", "George Orwell", 3, "9876543210", EstadoLibro(1))
        Libro.guardar_libros([libro])
        with open(self.test_csv, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            lineas = [fila for fila in reader]
        self.assertEqual(len(lineas), 2)
        self.assertEqual(lineas[1][0], "1984")
        self.assertEqual(lineas[1][1], "George Orwell")
        self.assertEqual(lineas[1][2], "3")
        self.assertEqual(lineas[1][3], "9876543210")
        self.assertEqual(lineas[1][4], "1")

    def test_buscar_libro_por_isbn(self):
        libros = [
            Libro("El Quijote", "Miguel de Cervantes", 5, "1234567890", EstadoLibro(0)),
            Libro("1984", "George Orwell", 3, "9876543210", EstadoLibro(1))
        ]
        encontrado = Libro.buscar_libro_por_isbn(libros, "1234567890")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.titulo, "El Quijote")
        no_encontrado = Libro.buscar_libro_por_isbn(libros, "9999999999")
        self.assertIsNone(no_encontrado)

if __name__ == "__main__":
    unittest.main()