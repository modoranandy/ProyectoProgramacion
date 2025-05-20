def _vaciar_csv(ruta):
    with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
        archivo.truncate(0)

def _vaciar_todos_los_csv():
    _vaciar_csv("config/alumnos.csv")
    _vaciar_csv("config/libros.csv")
    _vaciar_csv("config/cursos.csv")
    _vaciar_csv("config/prestamos.csv")
    print("Todos los CSVs han sido vaciados completamente.")