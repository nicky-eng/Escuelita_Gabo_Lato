def primeras_letras(cadena):
    """Función que devuelve la primera letra de cada palabra de la cadena ingresada."""
    nueva_cadena = ''
    espacio = False

    if cadena[0] !=' ':
        nueva_cadena = nueva_cadena + cadena[0]
    for i in cadena:
        if i == ' ':
            espacio = True
        else:
            if espacio == True:
                nueva_cadena = nueva_cadena + i          
                espacio = False

    return nueva_cadena
#Descomentar para probar la función.
#f = ' Nicolas   Andres Oyarzabal  '
#print(primeras_letras(f))

def mayuscula_en_primera_letra(cadena):
    """Función que capitaliza cada palabra de una cadena."""
    nueva_cadena = ''
    espacio = False

    if cadena[0] !=' ':
        nueva_cadena = nueva_cadena + cadena[0].upper()
    for i in cadena:
        if i == ' ':
            espacio = True
            nueva_cadena = nueva_cadena + i
        else:
            if espacio == True:
                nueva_cadena = nueva_cadena + i.upper()          
                espacio = False
            else: nueva_cadena = nueva_cadena + i

    return nueva_cadena    

#Descomentar para probar la función.
#f = ' nicolas  Andres oyarzabal  '
#print(mayuscula_en_primera_letra(f))

def palabras_comienzan_con_letra(cadena):
    """De una cadena, devuelve todas las palabras que comienzan con la letra especificada."""
    
    letra = 'a'
    nueva_cadena = ''
    espacio = True
    sumar_letras = False
    
    for i in cadena:
        if i.lower() == letra and espacio == True:
            sumar_letras = True
            nueva_cadena = nueva_cadena + i
        elif sumar_letras == True and i != ' ':
            nueva_cadena = nueva_cadena + i
        elif i == ' ' and sumar_letras == True: 
            espacio = True 
            sumar_letras = False
            nueva_cadena = nueva_cadena + i
        elif i == ' ':
            espacio = True        

    return nueva_cadena    

#Descomentar para probar la función.
mu = 'Ayer andábamos por el alambrado'
print(palabras_comienzan_con_letra(mu))
