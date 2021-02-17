"""Programa que devuelve el signo zodíaco correspondiente a una día y mes ingresado"""

dia = input('Ingrese el día de su cumpleaños:')
mes = input('Ingrese el mes su cumpleaños (en número):')

dia = int(dia)
mes = int(mes)

signos = ('Acuario', 'Piscis', 'Aries', 'Tauro', 'Geminis', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Escorpio', 'Sagitario', 'Capricornio')

if mes == 1:
    if dia >= 21:
        sz = 'Acuario'
    else:
        sz = 'Capricornio'
elif mes == 2:
    if dia >= 20:
        sz = 'Piscis'
    else:
        sz = 'Acuario'
elif mes == 3:
    if dia >= 21:
        sz = 'Aries'
    else:
        sz = 'Piscis'
elif mes == 4:
    if dia >= 21:
        sz = 'Tauro'
    else:
        sz = 'Aries'
elif mes == 5:
    if dia >= 21:
        sz = 'Géminis'
    else:
        sz = 'Tauro'
elif mes == 6:
    if dia >= 22:
        sz = 'Cáncer'
    else:
        sz = 'Géminis'
elif mes == 7:
    if dia >= 24:
        sz = 'Leo'
    else:
        sz = 'Cáncer'
elif mes == 8:
    if dia >= 24:
        sz = 'Virgo'
    else:
        sz = 'Leo'
elif mes == 9:
    if dia >= 24:
        sz = 'Libra'
    else:
        sz = 'Virgo'
elif mes == 10:
    if dia >= 23:
        sz = 'Escorpio'
    else:
        sz = 'Libra'
elif mes == 11:
    if dia >= 23:
        sz = 'Sagitario'
    else:
        sz = 'Escorpio'
else:
    if dia >= 22:
        sz = 'Capricornio'
    else:
        sz = 'Sagitario'

print(sz)   

