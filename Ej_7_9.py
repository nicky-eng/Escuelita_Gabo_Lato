def empaquetar(lista):
    """Se empaqueta la lista indicando, mediante tuplas, el valor que hay en la lista y la cantidad 
    de veces consecutivas que se repite ese valor."""

    contador = 0
    paquete = []

    aux = lista[0]
    
    for i in lista:
        if i == aux:
            contador += 1
        else: 
            paquete.append((aux, contador))
            aux = i
            contador = 1
    paquete.append((aux, contador))

    return paquete
            

#d = [1, 1, 1, 3, 5, 1, 1, 3, 3]
#print(empaquetar(d))    