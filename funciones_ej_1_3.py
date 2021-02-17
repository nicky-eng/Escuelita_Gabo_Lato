def perimetro(base, altura):
    """Calcula el perímetro de un rectángulo con los datos de su base y altura."""

    return (base+altura)*2

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo"""

    return base*altura

def area_coordenadas(x1, x2, y1, y2):
    """Calcula el área con las coordenadas cartesianas"""
    base1 = x2-x1
    altura1 = y2-y1
    return area_rectangulo(base1, altura1)

def perimetro_circulo(radio):
    """Calculo el perimetro del círculo de radio"""
    return (pi*2*radio)

def area_circulo(radio):
    """calcular el area de un circulo sólo con su radio"""
    return(pi*radio**2)

def volumen_esfera(radio):
    """calcula el volumen de una esfera con su radio"""
    return(pi*4/3*radio**3)

def hipotenusa(cateto1, cateto2):
    """Calcula la hipotenusa dados dos catetos"""
    return(sqrt(cateto1**2+cateto2**2))
