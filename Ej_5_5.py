"""Programa que implmenta el algortimo de Euclides para hallar el máximo compun divisor."""

# Se definen los  dos valores de los cuáles se va a hallar el mcd.
m = int(input('Ingrese un número entero: '))
n = int(input('Ingrese un número entero: '))

m0 = m # Se guardan las variables inicales para poder imprimir la respuesta y/o invertir su orden.
n0 = n

if m >= n: # Se busca que la división entera sea mayor o igual a 1.
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    print(n, " es el máximo común divisor de ", n0, " y ", m0, ".")

else:
    m, n = n, m
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    print(n, " es el máximo común divisor de ", n0, " y ", m0, ".")




