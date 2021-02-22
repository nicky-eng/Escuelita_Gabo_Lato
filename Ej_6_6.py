def solo_consonantes(cadena):
    """Función que devuelve sólo las letras consonantes de una cadena de caracteres."""
    
    consonantes = 'bcdfghjklmnpqrstvwxyz'
    nueva_cadena = ''
    for i in cadena:
        if i in consonantes:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

#string = 'logaritmos'
#print(solo_consonantes(string))

def solo_vocales(cadena):
    """Función que devuelve sólo las letras vocales de una cadena de caracteres."""
    
    vocales = 'aeiou'
    nueva_cadena = ''
    for i in cadena:
        if i in vocales:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

#string = 'logaritmos'
#print(solo_vocales(string))

def reemplazo_vocales(cadena):
    """Función que reemplaza cada vocal por su próxima vocal."""
    
    vocales = 'aeiou'
    reemplazos = {'a':'e', 'e':'i', 'i':'o', 'o':'u', 'u':'a'}
    nueva_cadena = ''
    for i in cadena:
        if i in vocales:
            nueva_cadena = nueva_cadena + reemplazos[i]
        else:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena
#vistaerou
#string = 'vestuario'
#print(reemplazo_vocales(string))

def reemplazo_vocales_sin_dic(cadena):
    """Función que reemplaza cada vocal por su próxima vocal sin usar diccionarios"""
       
    reemplazos = ['u', 'o', 'i', 'e', 'a']
    nueva_cadena = ''
    for i in cadena:
        if i in reemplazos:
            reemplazos.index(i)
            nueva_cadena = nueva_cadena + reemplazos[reemplazos.index(i)-1]
        else:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

#vistaeroueee
#string = 'vestuarioeee'
#print(reemplazo_vocales_sin_dic(string))

def es_palindromo(cadena):
    """Indica si la cadena ingresada es un palíndromo o no. Devuelve True/False."""
    nueva_cadena = ''
    cadena_sin_espacios = ''

    for i in cadena:
        if i != ' ':
            cadena_sin_espacios = cadena_sin_espacios + i
    
    for j in range(1, len(cadena_sin_espacios) + 1):
        nueva_cadena = nueva_cadena + cadena_sin_espacios[-j]
    
    print('Nueva cadena:', nueva_cadena)
    print('Cadena sin espacios:', cadena_sin_espacios)
    print(len(cadena_sin_espacios))
    temp = cadena_sin_espacios == nueva_cadena
    temp2 = cadena_sin_espacios is nueva_cadena
    print(temp, temp2)

    return (cadena_sin_espacios == nueva_cadena)

#d = 'anita lava la tina'
#print(es_palindromo(d))