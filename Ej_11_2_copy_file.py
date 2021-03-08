"""
Ejercicio 11.2. Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea
de texto o binario) a otro, de modo que quede exactamente igual.
Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.
"""

def cp(file):
    """
    Returns a copy of a text or binary file.

            Parameters:
                    file (text or binary): The file you want to copy.
            
            Returns: 
                    copy_Of_file (text or binary): A copy of the file.
    """

    import os

    dirname = os.path.dirname(__file__)
    copy = 'copy_of_'+ file

    with open(os.path.join(dirname, file), "rb") as my_file:
        with open(os.path.join(dirname, copy), "wb") as copy_file:
            data = my_file.read(16)
            check_empty = not data
            while check_empty != True:
                copy_file.write(data)
                data = my_file.read(16)
                check_empty = not data
                
    return 



    