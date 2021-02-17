def operaciones_matematicas(num1, num2):
    """Devuelve suma, resta, multiplica, division"""
    print("La suma de los números es: ", num1+num2)
    print("La resta de ellos es: ", num1-num2)
    print("La división del primero por el segundo es: ", num1/num2)
    print("Su producto es: ", num1*num2)


def tabla_multiplicar(num):
    """Devuelve la tabla de multiplicar del valor entero"""
    for i in range(1,11):
        print(num, " x ", i, " = ", num*i)
