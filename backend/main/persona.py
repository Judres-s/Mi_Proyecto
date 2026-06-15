from usuarios import Usuario

class Persona(Usuario):

    def __init__(self, nombreCompleto, edad):
        self.__nombreCompleto = nombreCompleto
        self.__edad = edad

    def getNombreCompleto(self):
        return self.__nombreCompleto

    def setNombreCompleto(self, nuevoNombre):
        self.__nombreCompleto = nuevoNombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, nuevaEdad):
        self.__edad = nuevaEdad

    def mostrarInformacion(self):
        print("Persona")
        print("Nombre:", self.__nombreCompleto)
        print("Edad:", self.__edad)