"""Ejercicio 8.1. Escribir una función que reciba una lista desordenada y un elemento, que:
a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de coincidencias encontradas.
b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
por parámetro y devuelva una lista con las posiciones."""

def count_coincidences(sequence, element):
    """
    Returns the amount of times the element is found in a sequence.

            Parameters:
                    sequence (list or tuple): A list of values to search through.
                    element (string or int): The value that is looked for.
                    
            Returns:
                    counter (int): The amount of times the element was found in the sequence.                    
    """

    counter = 0
    for value in sequence:
        if element == value:
            counter += 1
            
    return counter


def first_time_index(sequence, element):
    """
    Returns the index of the element the first time it is found in a sequence.

            Parameters:
                    sequence (list or tuple): A list of values to search through.
                    element (string or int): The value that is looked for.

            Returns:
                    index (int): The position of the element when it was first found in the sequence
                    or None if it wasn't found.                    
    """
    
    counter = 0
    found = False
    index = None

    for value in sequence:
        if value == element:
            found = True
            break
        else:
            counter += 1
    if found == True:
        index = counter
    else: 
        index = None

    return index

def coincidences_indexes(sequence, element):
    """
    Returns the indexes of the element everytime time it is found in a sequence using the
    previously defined first_time_index function.

            Parameters:
                    sequence (list or tuple): A list of values to search through.
                    element (string or int): The value that is looked for.

            Returns:
                    indexes (list): The positions of the element for everytime it was found in the sequence
                    or an empty list.                    
    """
    
    indexes = []
    aux_sequence = sequence
    aux_index = 0
    previous_aux_index = 0

    while aux_index != None:
        aux_index = first_time_index(aux_sequence, element)
        if aux_index != None:
            aux_sequence = aux_sequence [aux_index + 1 :]
            indexes.append(aux_index + previous_aux_index)
            previous_aux_index = aux_index + previous_aux_index + 1 
    
    return indexes
