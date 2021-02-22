
def separador_de_miles(numero):
    """Toma una cadena de números y agrega el punto separador de miles."""

    from Ej_6_2 import caracter_cada_tres as puntos

    numero = str(numero)

    numero = rev(numero)
    numero = puntos(numero, '.')
    numero = rev(numero)

    return numero

def rev(cadena):
    """ Devuelve la cadena pero al revés."""
    nueva_cadena = ''
    for i in range(1,len(cadena)+1):
        nueva_cadena = nueva_cadena + cadena [-i]

    return nueva_cadena

a = 1234567890

b = separador_de_miles(a)

print(b)