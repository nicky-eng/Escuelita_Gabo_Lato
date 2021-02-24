def generar_nombre(lista):
    """Función que genera una lista con cadenas del tipo "Nombre L. Apellido" a partir de una lista de tuplas."""

    lista_nombres = []

    for i in lista:
        if len(i) == 3:
            nombre = i[1] + ' ' + i[2] + '.' + ' ' + i[0]
            lista_nombres.append(nombre)
        elif len(i) == 2:
            nombre = i[1] + ' ' + i[0]
            lista_nombres.append(nombre)
    
    return lista_nombres


#d = (['Oyarzabal', 'Nicolas', 'A'], ['La Torre', 'Gabo'], ['Mirabella', 'María', 'P'])
#print(generar_nombre(d))