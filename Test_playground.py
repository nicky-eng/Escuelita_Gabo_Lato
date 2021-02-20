lista = ['Nico', 'Gato', 'Baba', 'Mati', 'Gato']

print(lista)

for index, nombre in enumerate(lista):
    if nombre == 'Gato':
        del lista[index]

print(lista)

