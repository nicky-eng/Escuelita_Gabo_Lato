def pedir_entero(mensaje, min, max):
    """Esta función pide un número entre el mínimo y el máximo y si el usuario ingresa uno fuera de ese rango
    se le vuelve a pedir un número"""
    
    min = int(min)
    max = int(max)
    
    print(mensaje, '[' ,min ,'..', max , ']:')
    z = int(input())

    while z < min or z > max:
        print('Por favor, ingresá un número entre ', min, 'y', max, '.')
        print(mensaje, '[' ,min ,'..', max , ']:')
        z = int(input())
        print (z)

    return z

    
mens = '¿Cuántos microgramos de GSL querés?'
min = 125
max = 1250

s = pedir_entero(mens, min, max)
