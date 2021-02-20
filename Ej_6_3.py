

def insertar_caracter(cadena, separador,maximo):
    """Para una cadena dada, inserta el separador entre cada una de las letras de esa cadena hasta un 'máximo' de veces."""
    nueva_cadena = ''
    contador = 0

    for i in cadena:
        if contador < maximo:
            nueva_cadena = nueva_cadena + (i + separador)
            contador += 1
        else:
            nueva_cadena = nueva_cadena + i

    return nueva_cadena

a = 'Nicolas_es_un_genio,_tío!'
caracter = '/'
maxi = 5

b = insertar_caracter(a, caracter, maxi)

print(b)

def espacios_por_separador(cadena, separador, maxi):
    """Reemplaza todos los espacios dentro de la cadena por el separador."""
    nueva_cadena = ''
    contador = 0

    for i in cadena:
        if i == ' ' and contador < maxi:
            nueva_cadena = nueva_cadena + separador
            contador += 1
        else:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

b = 'Nicolas es un genio, tío! Pero con todas las letras.'
caracter = '3'
maxi = 5

print(espacios_por_separador(b, caracter, maxi))



def numeros_por_caracter(cadena, caracter, maxi):
    """Reemplaza todos los número por el caracter."""
    nueva_cadena = ''
    contador = 0

    for i in cadena:
        if i.isdigit() == True and contador < maxi:
            nueva_cadena = nueva_cadena + caracter
            contador += 1
        else:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

c = 'N1col4s es un g3nio, 7ío! Per0 c0n tod4s las l3tr4s.'
caracter = '@'
maxi = 3

print(numeros_por_caracter(c, caracter, maxi))


def caracter_cada_tres(cadena, caracter, maxi):
    """Introduce el caracter en la cadena una vez cada 3 espacios."""
    nueva_cadena = ''
    contador = 0
    contador_reemplazos = 0
    
    for i in cadena:
        if contador % 3 == 0 and contador != 0 and contador_reemplazos < maxi:
            nueva_cadena = nueva_cadena + caracter + i
            contador_reemplazos += 1            
        else:
            nueva_cadena = nueva_cadena + i
        contador += 1
    
    return nueva_cadena

d = 'N1col4s es un g3nio, 7ío! Per0 c0n tod4s las l3tr4s.'
caracter = '$'
maxi = 6

print(caracter_cada_tres(d, caracter, maxi))