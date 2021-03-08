"""
Ejercicio 11.3. Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.
"""

def wc(file_name):
    """
    Prints how many lines, words, and characters a file has.

            Parameters:
                    file_name (text file): The complete name of the file that will be processed.

            Returns:
                    print (lines, words, characters): The amount of lines, words, and characters
                    excluding spaces that are present in the text.
    """

    import os

    dirname = os.path.dirname(__file__)

    lines = 0
    words = 0
    characters = 0
    
    with open(os.path.join(dirname, file_name), 'r') as file:
        for line in file:
            lines += 1
            words += len(line.split())

            for word in line.split():
                characters += len(word)
    
    print(lines, words, characters)
    
    return
            
