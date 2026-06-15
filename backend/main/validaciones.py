def validarEdad(edad):

    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    return edad

