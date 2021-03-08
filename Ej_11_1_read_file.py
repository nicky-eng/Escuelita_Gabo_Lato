"""
Ejercicio 11.1. Escribir una función, llamada head que reciba un archivo 
y un número N e imprima las primeras N líneas del archivo.
"""

def head(file, n):
    """
    Prints the first n lines of a file.
           
            Parameters:
                    file (text_file): File to read.
                    n (int): Number of lines to read.
        
            Outputs:
                    Prints the first n lines.
    """

    import os

    dirname = os.path.dirname(__file__)

    with open(os.path.join(dirname, file), "r") as f:
        for i in range(n):
            print(f.readline(), end="")

    return 