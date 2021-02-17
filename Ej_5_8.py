"""Programa que pide números hasta que se ingresa el -1 y despúes entrega la cantidad, suma, y promedio de números
ingresados por teclado."""

lista = []

centinela = input('Ingrese un número natural o ingres "-1" para terminar: ')

while centinela != '-1':
    lista.append(int(centinela))
    centinela = input('Ingrese un número natural o ingres "-1" para terminar: ')

if len(lista) >= 1:
    suma = 0
    for i in lista:
        suma = suma + i
    print('Se han ingresado ', len(lista), ' números, la suma de ellos es', suma, ' y su promedio es ', suma/len(lista), '.')

else:
    print('No se han ingresado datos a procesar.')

