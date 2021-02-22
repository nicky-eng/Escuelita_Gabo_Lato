def esta_ordenado_o_no(lista):
    """Esta función recibe una tupla y determina si está ordenada de menor a mayor o no devolviendo True o False"""
    ordenada = tuple(sorted(lista))
    return lista == ordenada

"""milista = (2, 4, 8, 5)

otralista = (2, 4, 5, 8)

listaletras = ('gato', 'pero', 'zebra')
otralistaletras = ('girafa', 'elefante', 'ave')

print(esta_ordenado_o_no(milista))
print(esta_ordenado_o_no(otralista))
print(esta_ordenado_o_no(listaletras))
print(esta_ordenado_o_no(otralistaletras))"""