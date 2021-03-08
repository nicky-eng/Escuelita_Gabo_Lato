
"""
Ejercicio 11.4. Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima
las líneas del archivo que contienen la cadena recibida.
"""

def grep(text, file_name):
    
    """Prints the lines that contain the given text.

            Parameters:
                    text (str): The text that has to be found in a line.
                    file_name (str): The complete name of the file.

            Returns:
                    print(line): Prints each line where the 'text' is found.
    """

    import os

    dirname = os.path.dirname(__file__)

    with open(os.path.join(dirname, file_name), 'r') as file:
        for line in file:
            if text.lower() in line.lower():
                print(line.rstrip())
    
    return