import os

def copia_seguridad():
    archivos = [
        "config/alumnos.csv",
        "config/libros.csv",
        "config/prestamos.csv",
        "config/admins.csv"
    ]

    for archivo in archivos:
        if os.path.exists(archivo):
            nombre_backup = f"{archivo}.backup"
            with open(archivo, 'r', encoding='utf-8') as f_origen, \
                 open(nombre_backup, 'w', newline='', encoding='utf-8') as f_destino:
                f_destino.write(f_origen.read())
            print(f"Copia de {archivo} guardada en {nombre_backup}")
        else:
            print(f"Advertencia: {archivo} no existe y no se ha copiado.")

    print("Copia de seguridad completada.")