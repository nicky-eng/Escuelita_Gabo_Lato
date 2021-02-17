def primeros_dos_caracteres(cadena):
    """Función que dada una cadena imprime los primeros dos caracteres."""
    print(cadena[:2])

def ultimos_tres_caracteres(palabra):
    """Función que imprime los últimos 3 caracteres."""
    print(palabra[-3:])

def cada_dos_caracteres(cadena):
    """Toda la cadena pero cada dos caracteres."""
    print(cadena[::2])

def cadena_al_reves(cadena):
    """ Imprime la cadena pero al revés."""
    for i in range(1,len(cadena)+1):
        print(cadena[-i], end='')
    print()

def cadena_plus_al_reves(cadena):
    """ Imprime la cadena pero al revés."""
    print(cadena, end='')
    for i in range(1,len(cadena)+1):
        print(cadena[-i], end='')
    print()