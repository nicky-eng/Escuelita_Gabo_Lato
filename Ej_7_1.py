def esta_ordenado_o_no(lista):
    """Esta función recibe una tupla y determina si está ordenada de menor a mayor o no devolviendo True o False"""
    ordenada = tuple(sorted(lista))
    return lista == ordenada

"""from Ej_7_12 import filter #Acá se está probando la función <filter>.

lista = [(2, 4, 8, 5), (2, 4, 5, 8), ('gato', 'pero', 'zebra'), ('girafa', 'elefante', 'ave') ]

print(filter(esta_ordenado_o_no, lista))"""


"""from Ej_7_12 import map #Acá se está probando el funcionamiento de la funicón <map>.

lista = [(2, 4, 8, 5), (2, 4, 5, 8), ('gato', 'pero', 'zebra'), ('girafa', 'elefante', 'ave') ]

d = map(esta_ordenado_o_no, lista)
print(d)"""

# Remover las triple comillas para probar la función diseñada.
"""milista = (2, 4, 8, 5)
otralista = (2, 4, 5, 8)
listaletras = ('gato', 'pero', 'zebra')
otralistaletras = ('girafa', 'elefante', 'ave')

print(esta_ordenado_o_no(milista))
print(esta_ordenado_o_no(otralista))
print(esta_ordenado_o_no(listaletras))
print(esta_ordenado_o_no(otralistaletras))"""