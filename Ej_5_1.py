"""Programa en el cual se ingresan notas, mientras el usuario quiera continuar, y al final se muestra el promedio de las notas."""

nota = input('Ingrese una nota: ')
nota = float(nota)

suma = 0

notas = [nota]

mas_notas = input('Desea ingresar más notas. Ingrese Si / No: ')

while mas_notas == 'si' or mas_notas == 'SI' or mas_notas == 'sí' or mas_notas == 'Si' or mas_notas == 'Sí':
    nota = input('Ingrese una nota: ')
    nota = float(nota)
    notas.append(nota)
    mas_notas = input('Desea ingresar más notas. Ingrese Si / No: ')

for i in range (len(notas)):
    suma = suma + notas [i]

suma = suma / len(notas)

print("El promedio de las notas ingresadas es: ", suma)
    

