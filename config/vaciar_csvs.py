import os

def vaciar_csv(ruta):
    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            archivo.truncate(0)
    except FileNotFoundError:
        print(f"Advertencia: No se encontró el archivo {ruta}")
    except Exception as e:
        print(f"Error al vaciar {ruta}: {e}")

def vaciar_todos_los_csv():

    archivos = [
        "config/alumnos.csv",
        "config/libros.csv",
        "config/prestamos.csv",
        "config/admins.csv"
    ]
    for archivo in archivos:
        if os.path.exists(archivo):
            vaciar_csv(archivo)
        else:
            print(f"Advertencia: El archivo {archivo} no existe.")
    print("Todos los CSVs han sido vaciados completamente.")