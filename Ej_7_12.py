def map(función, lista):
    """Devuelve una nueva lista con el resultado de aplicar la <función> a cada elemento de la <lista> de ingreso."""
    
    nueva_lista = []

    for i in lista:
        nueva_lista.append(función(i))
    
    return nueva_lista
    
def filter(función, lista):
    """Devuelve una nueva lista de aquellos elementos que, al aplicarles la <función>, devuelven el valor 'True'."""
    
    nueva_lista = []

    for i in lista:
        if función(i) == True:
            nueva_lista.append(i)
    
    return nueva_lista
