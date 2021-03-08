"""
Ejercicio 8.3. Agenda simplificada
Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo,
telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
Debe devolver una lista con todas las tuplas encontradas.
"""

def name_search(name, list):
    """Searches for the name inside the list of tuples.

            Parameters:
                    name (str): The entire name or just a part of it.

            Returns:
                    found_list (list of tuples): A list with all the tuples that
                    contained that string in the name part of the tuple.
    """
 
    found_list = []

    for value in list:
        if name.lower() in value[0]:
            found_list.append(value)
    
    return found_list
