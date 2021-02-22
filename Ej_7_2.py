def domino_encajan_tuplas(ficha1, ficha2):
    """Una función que devuelve 'True' si dos fichas de dominó encajan y devuelve 'False' si no lo hacen.
    Las fichas deben ingresarse como tuplas."""
   
    encajan = False

    if ficha1[0] in ficha2 or ficha1[1] in ficha2:
        encajan = True
    
    return encajan


#f1 = (0, 0)
#f2 = (2, 0)
#print(domino_encajan_tuplas(f1, f2))

def domino_encajan_cadena(ficha1, ficha2):
    """Una función que devuelve 'True' si dos fichas de dominó encajan y devuelve 'False' si no lo hacen.
    Las fichas deben ingresarse como cadenas. Ej: 2-3, 4-3."""
   
    encajan = False

    f1 = ficha1.split('-')
    f2 = ficha2.split('-')

    if f1[0] in f2 or f1[1] in f2:
        encajan = True
    
    return encajan

#fic1 = '2-4'
#fic4 = '3-6'
#print(domino_encajan_cadena(fic1, fic4))

