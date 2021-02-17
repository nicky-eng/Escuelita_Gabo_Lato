def esprimoono(num):
    """Función que dice si num es un numero primo o no."""

    num = int(num)
    noesprimo = False

    if num == 0 or num == 1:
        print("El número", num, "no es primo.")
    elif num == 2:
        print("El número ", num, " es primo.")
    else:
        maxdiv = num // 2 + 1
        for i in range (2, maxdiv):
            if num % i == 0:
                print("El número ", num, " no es primo.")
                noesprimo = True
                break
        if noesprimo == False:
            print("El número ", num, " es primo.")