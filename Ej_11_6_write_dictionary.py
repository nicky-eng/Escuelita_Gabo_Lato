"""
Ejercicio 11.6. Persistencia de un diccionario
a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
y el segundo como diccionario.
b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
y guarde el contenido del diccionario en el archivo, con el formato clave, valor.
"""

def load_data(file_name):
    """
    Loads a dictionary from a text file.
    """

    import os

    dirname = os.path.dirname(__file__)
    my_dictionary = {}

    with open(os.path.join(dirname, file_name), 'r') as my_file:
        for line in my_file:
            entry = line.split()
            my_dictionary[entry[0]] = entry[1]
    
    return my_dictionary

            

def save_data(dictionary, file_name):
    """
    Saves a dictionary to a text file.
    """

    import os

    dirname = os.path.dirname(__file__)
    
    with open(os.path.join(dirname, file_name), 'a+') as my_file:
        for entry in dictionary:
            new_line = entry + ' ' + dictionary[entry]
            my_file.write(new_line + '\n')
            
    return