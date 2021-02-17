def multiplos_for(num1, num2):
    """Función que devuelve cuántos múltiplos de num1 hay menores que num2, utilizando un loop for para
    encontrarlos."""
    contador = 0 # Inicializamos el contador de múltiplos.
    for i in range(num1, num2, num1): # Aumentamos de a múltiplos del num1, pero da error si num1 = 0.
        if i < num2:
            contador += 1

    return (contador)

def multiplos_while(num1, num2):
    """Función que devuelve cuántos múltiplos de num1 hay menores que num2, utilizando un loop while para
    encontrarlos."""
    contador = 0 # Inicializamos el contador de múltiplos.
    multiplicador = 1 # Inicializamos la variable que va a multiplicar a nuestro primer número.
    while num1 * multiplicador < num2:
        contador += 1
        multiplicador += 1

    return(contador)
