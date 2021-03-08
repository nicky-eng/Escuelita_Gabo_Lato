"""
Ejercicio 8.2. Escribir una función que reciba una lista de números no ordenada, que:
a) Devuelva el valor máximo.
b) Devuelva una tupla que incluya el valor máximo y su posición.
c) ¿Qué sucede si los elementos son cadenas de caracteres?
Nota: no utilizar lista.sort()
"""
from typing import Sequence


def max_value(sequence):
    """
    Returns maximum value of an unsorted sequence.
    
            Parameters:
                    sequence (list): Sequence of numbers or strings.

            Returns:
                    maximum (int or string): The maximum alphanumerical value found in the sequence.
    """
    maximum = sequence[0]
    for value in sequence:
        value = str(value)
        if value > maximum:
            maximum = value
    
    return maximum

def max_value_with_index (sequence):

    """
    Returns maximum value of an unsorted sequence with it's corresponding index.

            Parameters:
                    sequence (list): Sequence of numbers or strings.

            Returns:
                    maximum_index (tuple): A tuple with the maximum alphanumerical value
                    found in the sequence and it's index.
    """
    index = 0
    maximum = sequence[0]
    for value in sequence:
        value = str(value)
        if value > maximum:
            maximum = value
        index += 1
    
    return (maximum, index)

