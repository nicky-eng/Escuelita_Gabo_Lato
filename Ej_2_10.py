"""Imprimir todas las 28 fichas de dominó sin repetir"""
print("Ingresar hasta qué número se quieren las fichas de dominó")
num=input()
num=int(num)+1

for i in range(num):
    for e in range (i,num):
        print("[",i,"|",e,"]")