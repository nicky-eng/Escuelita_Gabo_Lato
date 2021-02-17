# Suponiendo que el primer día del año fue lunes, escribir una función que reciba
# un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
# si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.

def dia_de_semana(numero):
    """Dado el número con el día del año, devuelve el día de la semana correspondiente, sabiendo
     que el año arrancó un lunes."""

    dias = ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo')

    dia = (numero % 7) - 1

    return (dias[dia])

