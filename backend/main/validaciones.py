def validarEdad(edad):

    if edad < 8:
        raise ValueError("La edad no puede ser menor de 8")

    return edad

