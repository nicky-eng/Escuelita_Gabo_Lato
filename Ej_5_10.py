
import esprimo_boolean

def primos_hasta(num):
    """Esta función toma un número natural y devuelve todos los números primos que hay hasta ese número inclusive."""

    lista_primos = []
    num = int(num)
    for i in range (1, num +1):
        primo = esprimo_boolean.esprimo_bool(i)
        if primo == False:
            lista_primos.append(i)

    print(lista_primos)