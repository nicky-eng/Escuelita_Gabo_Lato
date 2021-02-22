def es_subcadena(cadena, subcadena):
    """Función que se fija si la <subcadena> está dentro de la <cadena> y devuelve True o False."""

    return subcadena in cadena

#a = 'nando'
#b = 'Fernando'
#print(es_subcadena(b, a))

def orden_alfa(cadena1, cadena2):
    """Dadas dos cadenas, devuelve la que esté primera en orden alfabético."""
    menor_encontrada = False #Pongo un testigo por si no se encuentra una palabra menor que otra mientras se recorre el for loop.

    if len(cadena1) >= len(cadena2): #Determino cuál palabra es más corta para no tener un "out of range" en el for loop.
        for_range = len(cadena2)
        palabra_corta = cadena2
    else:
        for_range = len(cadena1)
        palabra_corta = cadena1

    for i in range(for_range): 
        if cadena1[i] < cadena2[i]:
            return (cadena1)
            menor_encontrada = True
        elif cadena1[i] > cadena2[i]:
            return(cadena2)
            menor_encontrada = True
        else:
            continue
    if menor_encontrada == False:
        return palabra_corta #Si hasta la última letra del for loop, las dos palabras eran iguales, devuelve la más corta.

#ad1 = 'gnome'
#cad2 = 'kde'
#print(orden_alfa(cad1, cad2))