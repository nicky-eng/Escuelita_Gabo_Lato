"""
Ejercicio 11.5. Escribir una función, llamada rot13, que reciba un archivo de texto de origen
y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada
en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter 
comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un
nuevo caracter.
"""

def rot13(origin_file, destination_file):
    """
    Encripts the text from origin to the destination file.
    """

    import os

    dirname = os.path.dirname(__file__)

    with open(os.path.join(dirname, origin_file), 'r') as my_file:
        with open(os.path.join(dirname, destination_file), 'a+') as destiny:
            destiny.write('\n' * 2)
            for line in my_file:
                encripted_line = ''
                for character in line:
                    if character.isalpha():
                        encripted_char = chr(ord(character) + 3)
                        encripted_line = encripted_line + encripted_char
                    else:
                        encripted_line = encripted_line + character
                destiny.write(encripted_line)

    return