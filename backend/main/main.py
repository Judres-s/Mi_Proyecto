from estudiante import Estudiante
from validaciones import validarEdad

def main():

    try:

        nombreCompleto = input("Ingrese el nombre del estudiante: ")

        edad = int(input("Ingrese la edad: "))

        validarEdad(edad)

        programa = input("Ingrese el programa: ")

        estudiante = Estudiante(nombreCompleto, edad, programa)

        print()
        estudiante.mostrarInformacion()

    except ValueError as error:

        print()
        print("Error:", error)

if __name__ == "__main__":
    main()
