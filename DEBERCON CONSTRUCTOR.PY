class Estudiante:
    def __init__(self, nombre, edad, matricula, carrera, cursos, promedio):
        """
        Constructor: Inicializa los atributos del estudiante.
        """
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.cursos = cursos
        self.promedio = promedio
        print(f"Estudiante '{self.nombre}' con matrícula '{self.matricula}' ha sido creado.")

    def __del__(self):
        """
        Destructor: Limpia cuando el objeto es destruido.
        """
        print(f"Estudiante '{self.nombre}' con matrícula '{self.matricula}' ha sido eliminado.")

    def mostrar_informacion(self):
        """
        Muestra la información del estudiante.
        """
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Matrícula: {self.matricula}, "
              f"Carrera: {self.carrera}, Cursos: {self.cursos}, Promedio: {self.promedio}")

    def actualizar_promedio(self, nuevo_promedio):
        """
        Actualiza el promedio del estudiante.
        """
        self.promedio = nuevo_promedio
        print(f"Promedio de {self.nombre} ha sido actualizado a {self.promedio}")

    def agregar_curso(self, nuevo_curso):
        """
        Agrega un nuevo curso a la lista de cursos del estudiante.
        """
        self.cursos.append(nuevo_curso)
        print(f"Curso '{nuevo_curso}' ha sido agregado a la lista de cursos de {self.nombre}")

def crear_estudiante():
    """
    Crea un estudiante con datos ingresados por el usuario.
    """
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    matricula = input("Ingrese la matrícula del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    cursos = input("Ingrese los cursos del estudiante (separados por comas): ").split(',')
    promedio = float(input("Ingrese el promedio del estudiante: "))
    
    return Estudiante(nombre, edad, matricula, carrera, cursos, promedio)

print("Ingrese los datos del primer estudiante:")
estudiante1 = crear_estudiante()

print("\nIngrese los datos del segundo estudiante:")
estudiante2 = crear_estudiante()

print("\nInformación de los estudiantes:")
estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()

nuevo_promedio = float(input(f"\nIngrese el nuevo promedio para {estudiante1.nombre}: "))
estudiante1.actualizar_promedio(nuevo_promedio)

nuevo_curso = input(f"Ingrese un nuevo curso para {estudiante2.nombre}: ")
estudiante2.agregar_curso(nuevo_curso)

del estudiante1

