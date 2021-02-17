def esprimo_bool2(num):
    """Función que determina si num es un número primo o no y devuelve True si lo es, y False si no lo es"""

    num = int(num)
    esprimo = True

    if num == 0 or num == 1:
        esprimo = False
    elif num == 2:
        esprimo = True
    else:
        maxdiv = num // 2 + 1 # Sé que jamás va a ser divisible por más que su mitad. Y le sumo uno, para que esa parte sea incluida en el for loop.
        for i in range (2, maxdiv):
            if num % i == 0:
                esprimo = False
                break

    return (esprimo)

def esprimo_bool(num):
    """Función que dice si num es un numero primo o no."""

    num = int(num)
    noesprimo = False

    if num == 0 or num == 1:
        noesprimo = True
    elif num == 2:
        noesprimo = False
    else:
        maxdiv = num // 2 + 1
        for i in range (2, maxdiv):
            if num % i == 0:
                noesprimo = True
                break
    return (noesprimo)
