def mayorproducto(num1, num2, num3, num4):
    """Esta función toma 4 números enteros y devuelve el mayor producto que se puede lograr con ellos."""
 
    num1=int(num1)
    num2=int(num2)
    num3=int(num3)
    num4=int(num4)

    num_list=[num1, num2, num3, num4]

    mayorprod = num1*num2

    for i in range(4):
        for h in range(i+1,4):
            producto=num_list[i]*num_list[h]
            if producto > mayorprod:
                mayorprod = producto
    
    return mayorprod

