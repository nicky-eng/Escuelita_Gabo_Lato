def tuplas_a_dic(lista):
    """Toma una lista de tuplas y genera un diccionario donde las claves son
    el primer elemnto de la tupla y los valores una lista de los demás elementos."""

    diccionario ={}
    lista_aux = []
    for i in lista:
        lista_aux.append(i[1])
        if i[0] in diccionario:
            diccionario[i[0]] = diccionario[i[0]] + lista_aux
        else:
            diccionario[i[0]] = [i[1]]
        lista_aux = []
    return diccionario


mi_lista = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
d = print(tuplas_a_dic(mi_lista))