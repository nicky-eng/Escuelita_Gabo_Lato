"""Hay que adivinar la contraseña o no podés seguir con tu vida, pero ahora solo tenés 5 intentos."""
import time

contraseña = 'nickypass' # Si usted es un hacker, no espíe este valor.

intentos = 1
max_intentos = 5 # La cantidad máxima de veces que se permite ingresar una contraseña entes de bloquear el acceso.

trypass = input('Ingrese la contraseña: ')

while trypass != contraseña and intentos < max_intentos:
    time.sleep(2*intentos)
    print('Contraseña incorrecta.')
    trypass = input('Ingrese la contraseña: ')
    intentos += 1

if trypass == contraseña:
    print('Contraseña aceptada. Puede continuar con su vida. ¡Sea feliz!')
else:
    time.sleep(2*intentos)
    print('Usted ingresó una contraseña incorrecta más de ', (max_intentos - 1), ' veces. Su cuenta fue bloqueda. ' )