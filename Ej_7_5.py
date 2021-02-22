def listar_primos(lista):
    """De una lista de números, devuelve otra lista de todos aquellos que son primos."""

    from esprimo_boolean import esprimo_bool2
    
    lista_primos = []

    for i in lista:
        if esprimo_bool2(i) == True:
            lista_primos.append(i)
    
    return lista_primos

#d = [1, 2, 3, 4, 5, 6, 7, 17, 22, 23, 28]
#print(listar_primos(d))

def sumaypromedio(lista):
    """Devuelve la sumatoria y el promedio de los números de la lista."""
    
    sumatoria = 0

    for i in lista:
        sumatoria = sumatoria + i
    
    promedio = sumatoria / len(lista)

    return sumatoria, promedio

#d = [2, 3, 4, 5, 6, 7, 17, 22, 23, 10000]
#print(sumaypromedio(d))

def lista_factorial(lista):
    """Devuelve una lista con el factorial de cada número de una lista de números."""
    
    lista_factoriales = []
    
    for i in lista:
        factorial = 1
        for j in range (1,i+1):
            factorial = factorial * j
        lista_factoriales.append(factorial)
    
    return lista_factoriales

#d = [0, 1, 2, 3, 4, 5, 6, 7, 17, 22, 23,]
#print(lista_factorial(d))
