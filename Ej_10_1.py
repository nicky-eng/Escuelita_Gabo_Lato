"""
Ejercicio 10.1. Analizar cada una de las siguientes funciones. ¿Cuál es el contrato de la función?
¿Cómo sería su documentación? ¿Es necesario agregar comentarios? ¿Se puede simplificar el
código y/o mejorar su legibilidad? ¿Hay algún invariante de ciclo?
"""

def Abs(i):
    if i >= 0:
    return i
else:
return -i