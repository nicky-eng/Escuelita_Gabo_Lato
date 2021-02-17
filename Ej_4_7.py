
def secuencia_romana(num, unit, unit_x_5, unit_x_10 ):
    """Define qué símbolos hay que presentar y cómo se ordenan para cada dígito de
    las centenas, decenas y unidades, donde unit, unit_x_5 y unit_x_10 HAY QUE DEFINIRLOS como 'I', 'V','X' para
    las unidades, 'X', 'L', 'C' para las decenas y 'C', 'D', 'M' para las centenas."""
    
    if num == 0:
        rom = ''
    elif num > 0 and num < 4:
        rom = unit * num
    elif num == 4:
        rom = unit + unit_x_5
    elif num == 5:
        rom = unit_x_5
    elif num > 5 and num < 9:
        rom = unit_x_5 + unit * (num - 5)
    else:
        rom = unit + unit_x_10

    return(rom)

def numero_a_romano(año):
    """ Toma un número de un año entre 1 y 3999 y lo convierte a números romanos."""

    año = int(año)

    if año > 3999:
        return (print("El año ingresado excede la capacidad de conversión del sistema."))

    # Se descompone el número para poder cifrarlo.
        
    millares = año // 1000
    centenas = (año % 1000) // 100
    decenas = (año % 100) // 10
    unidades = año % 10
     
    millares_romano = 'M' * millares # Millares a romanos. No se usa la función "secuencia_romana" porque no excedemos el valor de 3.
    
    centenas_romano = secuencia_romana(centenas, 'C', 'D', 'M')  # Centenas a numeros romanos.

    decenas_romano = secuencia_romana(decenas, 'X', 'L', 'C') # Decenas a números romanos.

    unidades_romano = secuencia_romana(unidades, 'I', 'V','X') # Unidades a números romanos.

    año_romano = millares_romano + centenas_romano + decenas_romano + unidades_romano

    return (año_romano)

año = input('Ingrese un año entre 1 y 3999:')
print(numero_a_romano(año))