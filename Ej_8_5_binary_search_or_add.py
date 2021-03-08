"""
Ejercicio 8.5. Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverla. Si
no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
(No utilizar lista.sort().)
"""
def binary_search_or_add(sequence, element):
    """
    Returns the position of the element, and if not found, it inserts it in the correct position.

            Parameters:
                    sequence (list): A sorted list of elements.
                    element (str or int): The element to look for.
            
            Returns:
                    middle (int): The index of the searched element or the position of where it was placed
                    if it was not found.
    """

    left = 0
    right = len(sequence) - 1

    while left <= right:
        middle = (left + right) // 2

        if sequence[middle] == element:
            return middle
        
        if sequence[middle] < element:
            left = middle + 1
        else:
            right = middle - 1 

    if element < sequence[middle]:
        sequence.insert(middle, element)
    else:
        sequence.append(element)
        middle += 1
    print(sequence)

    return middle
