def invertir_lista(lista):
    """Devuelve una nueva lista como la original pero invertida."""

    lista_nueva = []
    
    for i in range(1,len(lista)+1):
        lista_nueva.append(lista[-i])
    
    return lista_nueva

#t = ['Ahora', 'vamos', 'a', 'correr', 'rápido.']
#print(invertir_lista(t))

def invertir_lista_sin_aux(lista):
    """Devuelve una nueva lista como la original pero invertida, sin utilizar listas auxiliares en el código."""

    for i in range(1,len(lista)+1):
        lista.append(lista[-i])
        lista.remove(lista[-i-1])
    
    return lista

t = ['Ahora', 'vamos', 'a', 'correr', 'rápido.']
print(invertir_lista_sin_aux(t))