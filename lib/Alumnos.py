import csv
from lib.Cursos import Curso
from config.config import NivelCurso, Tramos, Bilingue


class Alumno:

    RUTA_CSV = "config/alumnos.csv"
    CAMPOS = ["dni", "nombre", "apellido", "edad","tramo", "bilingue", "curso", "nivel", "letra"]

    def __init__(self, nombre:str = "Alumno", apellido:str = "0", edad:int = 0, tramo: Tramos | None = None,
                 dni:str = "000000000X",curso: Curso | None = None, bilingue:Bilingue | None = None):
        self.nombre:str = str(nombre).upper()
        self.apellido:str = str(apellido).upper()
        self.edad:int = int(edad)
        self.tramo:Tramos = tramo if tramo in Tramos else Tramos.NINGUNO
        self.dni:str = str(dni).upper()
        self.curso: Curso = curso if isinstance(curso,Curso) else Curso()
        self.bilingue:Bilingue = bilingue if bilingue in Bilingue else Bilingue.NO

    def __str__(self):
        return (f"Alumno: {self.nombre},{self.apellido}, con DNI/NIE {self.dni} de {self.edad} "
                f"años, esta cursando {self.curso} con el Tramo {self.tramo} y {self.bilingue} ")

    def __eq__(self, other):
        if isinstance(other, Alumno):
            return self.dni == other.dni
        return False

    @staticmethod
    def add_new_alumno():
        nombre = input("Nombre del Alumno: ")
        apellido = input("Apellido del Alumno: ")
        edad = int(input("Edad del Alumno: "))
        dni = input("DNI/NIE del Alumno: ")
        print("Opciones de Tramo:")
        for t in Tramos:
            print(f"{t.value}: {t.name}")
        tramo = int(input("Tramo del Alumno: "))
        print("Opciones de Bilingüe:")
        for b in Bilingue:
            print(f"{b.value}: {b.name}")
        bilingue = int(input("El Alumno es bilingue: "))
        curso = int(input("Curso del Alumno: "))
        nivel = int(input("Nivel del Alumno: "))
        letra = str(input("Letra del Alumno: "))
        curso = Curso(curso,NivelCurso(nivel),letra)
        tramo = Tramos(tramo)
        bilingue = Bilingue(bilingue)
        return Alumno(nombre, apellido, edad, tramo, dni, curso,bilingue)

    @staticmethod
    def buscar_alumno_por_dni(alumnos, dni):
        for alumno in alumnos:
            if alumno.dni == dni:
                return alumno
        return None

    @staticmethod
    def eliminar_alumno(alumnos, dni):
        alumno = Alumno.buscar_alumno_por_dni(alumnos, dni)
        if alumno:
            alumnos.remove(alumno)
            Alumno.guardar_alumnos(alumnos)
            print("Alumno eliminado correctamente.")
            return True
        else:
            print("No se ha encontrado ningún alumno con ese DNI/NIE.")
            return False

    @staticmethod
    def cargar_alumnos():
        alumnos = []
        try:
            with open(Alumno.RUTA_CSV, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for i, fila in enumerate(reader):
                    if not fila or len(fila) < 9:
                        continue
                    if i == 0 and fila[3].lower() == "edad":
                        continue
                    try:
                        curso_obj = Curso(
                            int(fila[6]),
                            NivelCurso(int(fila[7])),
                            fila[8]
                        )
                        tramo_enum = Tramos(int(fila[4]))
                        bilingue_enum = Bilingue(int(fila[5]))
                        alumnos.append(Alumno(
                            nombre=fila[1],
                            apellido=fila[2],
                            edad=int(fila[3]),
                            tramo=tramo_enum,
                            dni=fila[0],
                            curso=curso_obj,
                            bilingue=bilingue_enum
                        ))
                    except Exception as e:
                        print(f"Error en la fila {i + 1}: {fila}. Detalle: {e}")
        except FileNotFoundError:
            pass
        return alumnos

    @staticmethod
    def guardar_alumnos(alumnos):
        with open(Alumno.RUTA_CSV, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(Alumno.CAMPOS)
            for alumno in alumnos:
                writer.writerow([
                    alumno.dni,
                    alumno.nombre,
                    alumno.apellido,
                    alumno.edad,
                    alumno.tramo.value,
                    alumno.bilingue.value,
                    alumno.curso.curso,
                    alumno.curso.nivel.value,
                    alumno.curso.letra
                ])


def editar_alumno(alumnos):
    dni = input("Introduce el DNI/NIE del alumno que deseas editar: ").upper()
    alumno = None
    for a in alumnos:
        if a.dni == dni:
            alumno = a
            break
    if not alumno:
        print("No se ha encontrado ningún alumno con ese DNI/NIE.")
        return

    print(f"\nEditando alumno: {alumno.nombre} {alumno.apellido} (DNI: {alumno.dni})")

    nuevo_nombre = input(f"Nombre [{alumno.nombre}]: ")
    nuevo_apellido = input(f"Apellido [{alumno.apellido}]: ")
    nueva_edad = input(f"Edad [{alumno.edad}]: ")

    print("Opciones de Tramo:")
    for t in Tramos:
        print(f"{t.value}: {t.name}")
    nuevo_tramo = input(f"Tramo [{alumno.tramo.value}]: ")

    print("Opciones de Bilingüe:")
    for b in Bilingue:
        print(f"{b.value}: {b.name}")
    nuevo_bilingue = input(f"Bilingüe [{alumno.bilingue.value}]: ")

    nuevo_curso = input(f"Curso [{alumno.curso.curso}]: ")
    nuevo_nivel = input(f"Nivel [{alumno.curso.nivel.value}]: ")
    nueva_letra = input(f"Letra [{alumno.curso.letra}]: ")

    if nuevo_nombre:
        alumno.nombre = nuevo_nombre.upper()
    if nuevo_apellido:
        alumno.apellido = nuevo_apellido.upper()
    if nueva_edad:
        alumno.edad = int(nueva_edad)
    if nuevo_tramo:
        alumno.tramo = Tramos(int(nuevo_tramo))
    if nuevo_bilingue:
        alumno.bilingue = Bilingue(int(nuevo_bilingue))
    if nuevo_curso:
        alumno.curso.curso = int(nuevo_curso)
    if nuevo_nivel:
        alumno.curso.nivel = NivelCurso(int(nuevo_nivel))
    if nueva_letra:
        alumno.curso.letra = nueva_letra.upper()

    print("Alumno editado correctamente.")
    Alumno.guardar_alumnos(alumnos)