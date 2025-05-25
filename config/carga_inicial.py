import csv
import os

def crear_csv_con_cabecera(ruta, cabecera):
    if not os.path.exists(ruta):
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(cabecera)

def carga_inicial():

    from lib.Alumnos import Alumno
    from lib.Libros import Libro
    from lib.Prestamos import Prestamo
    from lib.Admins import Admin

    crear_csv_con_cabecera("config/alumnos.csv", Alumno.CAMPOS)
    crear_csv_con_cabecera("config/libros.csv", Libro.CAMPOS)
    crear_csv_con_cabecera("config/prestamos.csv", Prestamo.CAMPOS)
    crear_csv_con_cabecera("config/admins.csv", Admin.CAMPOS)

    print("Carga inicial de archivos completada.")
