def binario_a_decimal(numero):
    """Toma un número escrito en binario y lo pasa a decimal."""
    numero_decimal = 0
    posicion = 0

    for i in range(1, len(numero)+1):
        numero_decimal = numero_decimal + (2 ** posicion) * int(numero[-i])
        posicion += 1
    return numero_decimal

#n = '1010'
#print(binario_a_decimal(n))
        
