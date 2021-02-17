#Nicky O. Guía de Ejercicios 3.2
"""Calcula la suma de los tiempos de dos intervalos de tiempo dados usando las funciones definidas en Ej_3_1"""
from Ej_3_1 import *

hora1=int(input("Ingrese las horas del intervalo 1:"))
minu1=int(input("Ingrese los minutos del intervalo 1:"))
segu1=int(input("Ingrese los segundos del intervalo 1:"))

hora2=int(input("Ingrese las horas del intervalo 2:"))
minu2=int(input("Ingrese los minutos del intervalo 2:"))
segu2=int(input("Ingrese los segundos del intervalo 2:"))

tiempo_total = (calcseg(hora1,minu1,segu1) + calcseg(hora2,minu2,segu2))
tiempo_total = calctiempo((tiempo_total))

print(tiempo_total)
