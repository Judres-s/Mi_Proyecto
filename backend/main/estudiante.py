from persona import Persona

class Estudiante(Persona):

    def __init__(self, nombreCompleto, edad, programa):
        super().__init__(nombreCompleto, edad)
        self.programa = programa

    def mostrarInformacion(self):
        print(" INFORMACIÓN DEL ESTUDIANTE")
        print("Nombre:", self.getNombreCompleto())
        print("Edad:", self.getEdad())
        print("Programa:", self.programa)