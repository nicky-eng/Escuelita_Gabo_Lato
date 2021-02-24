def suma_matrices(a, b):
    """Devuelve la suma de dos matrices ingresadas como lista de las filas en lista."""

    suma = []

    for i in range(len(a)):
        fila_aux = []
        for j in range(len(a[i])):        
            fila_aux.append(a[i][j] + b[i][j])
        suma.append(fila_aux)

    return suma
"""
a = [[3, 7, 2, 3],
     [4, 8, 9, 6],
     [3, 1, 4, 1]]

b = [[4, 9, 12, 4],
     [14, 0, 5, 2],
     [5, 3, 6, 2]]

print(suma_matrices(a, b))
"""

def multiplicacion_de_matrices(a, b):
    """Función que devuelve la multiplicación de dos matrices de m*n y n*p."""
    
    if len(a[0]) != len(b):
        print("El número de columnas de A no es igual al número de filas de B. Las matrices no son multiplicables.")
        
        return None
    else:

        matriz_producto = []

        for i in range(len(a)):
            fila_i = []
            for j in range(len(b[0])):
                cij = 0
                for r in range(len(b)):
                    cij = cij + a[i][r] * b[r][j]
                fila_i.append(cij)
            matriz_producto.append(fila_i)

        return matriz_producto        

"""a = [[3, 2],
     [4, 1],
     [5, 7]]

b = [[4, 6, 7],
     [1, 5, 3]]"""

a = [[3, 7],
     [4, 8],
     [3, 1],
     [2, 0]]

b = [[4, 9, 12, 3],
     [14, 0, 5, 1],]

print(multiplicacion_de_matrices(a, b))