def ordenar_mayor_menor_igual(lista, k):
    """A partir de la lista devuelve 3 listas, con los números menores, mayores e iguales a k."""

    lista_menores = []
    lista_mayores = []
    lista_iguales = []

    for i in lista:
        if i < k:
            lista_menores.append(i)
        elif i > k:
            lista_mayores.append(i)
        else:
            lista_iguales.append(i)
    
    return lista_menores, lista_mayores, lista_iguales

#d = [2, 4, 8, 12, 11, 12, 12, 15, 18, 15]
#r = 14
#print(ordenar_mayor_menor_igual(d, r))

def lista_multiplos_de_k(lista, k):
    """A partir de la lista devuelve una lista con los múltiplos de k."""

    lista_multiplos = []

    for i in lista:
        if i % k == 0:
            lista_multiplos.append(i)

    return lista_multiplos

#d = [2, 4, 8, 12, 11, 12, 12, 15, 18, 15]
#r = 2
#print(lista_multiplos_de_k(d, r))

