def producto_escalar(a,b):
    """Función que efectúa el producto escalar entre 2 vectores de n componentes."""
    
    producto = 0

    if len(a) != len(b):
        print("Los vectores son de dimensiones diferentes. No se pueden multiplicar.")
    else:
        for i in range(len(a)):
            producto = producto + a[i] * b[i]
    
    return producto

#d = (3, 5, -2)
#e = (4, -9, 3)
#print(producto_escalar(d, e))

def son_ortogonales(a, b):
    """Función que recibe dos vectores y devuelve si son ortogonales "True" o no "False". """
   
    if producto_escalar(a, b) == 0:
        ortogonales = True
    else:
        ortogonales = False
    
    return ortogonales

#d = (0, 0, 5)
#e = (4, 4, 0)
#print(son_ortogonales(d, e))

def son_paralelos(a, b):
    """Función que recibe dos vectores y devuelve si son paralelos "True" o no "False". """
    
    import math

    norma_a = 0
    norma_b = 0

    # Cálculo de las normas de a y b
    for i in range(len(a)):
        norma_a = norma_a + a[i] ** 2
    norma_a = math.sqrt(norma_a)

    for i in range(len(b)):
        norma_b = norma_b + b[i] ** 2
    norma_b = math.sqrt(norma_b)

    var1 = norma_a * norma_b

    if abs((abs(producto_escalar(a, b)) - var1)) <= 0.000000001: #Para evitar problemas de comparaciones con valores de punto flotante, se usa el menor que un error determiando.
        paralelos = True
    else:
        paralelos = False
    
    return paralelos

#d = (1, 1, 0)
#e = (4, 4, 0)
#print(son_paralelos(d, e))

def norma_vector(a):
    """Devuelve la norma de un vector."""
    import math
    norma = 0
    for i in a:
        norma = norma + i ** 2
    norma = math.sqrt(norma)
    
    return norma

#d = (5, 8, 9)
#print(norma_vector(d))