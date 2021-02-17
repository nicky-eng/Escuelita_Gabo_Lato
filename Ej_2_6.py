from espar import*

"""Programa que imprime todos los números pares entre dos números dados por el ususario"""
print("Ingrese un número entero.")
num1=input()
print("Ingrese un número entero mayor que el anterior")
num2=input()

num1= int(num1)
num2= int(num2)+1

i=num1

for i in range(num1, num2):
    espar(i)
    i=i+1
   

