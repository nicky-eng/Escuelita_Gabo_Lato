def insertar_caracter(cadena, separador):
    """Para una cadena dada, inserta el separador entre cada una de las letras de esa cadena."""
    nueva_cadena = ''
    for i in cadena:
        nueva_cadena = nueva_cadena + (i + separador)
            
    return nueva_cadena

def epacios_por_separador(cadena, separador):
    """Reemplaza todos los espacios dentro de la cadena por el separador."""
    nueva_cadena = ''
    for i in cadena:
        if i == ' ':
            nueva_cadena = nueva_cadena + separador
        else:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

def numeros_por_caracter(cadena, caracter):
    """Reemplaza todos los número por el caracter."""
    nueva_cadena = ''
    for i in cadena:
        if i.isdigit() == True:
            nueva_cadena = nueva_cadena + caracter
        else:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

def caracter_cada_tres(cadena, caracter):
    """Introduce el caracter en la cadena una vez cada 3 espacios."""
    nueva_cadena = ''
    contador = 0
    for i in cadena:
        if contador % 3 == 0 and contador != 0:
            nueva_cadena = nueva_cadena + caracter + i            
        else:
            nueva_cadena = nueva_cadena + i
        contador += 1
    
    return nueva_cadena