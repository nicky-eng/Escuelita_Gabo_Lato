def mayorproducto(num1, num2, num3, num4):
    """Esta función toma 4 números enteros y devuelve el mayor producto que se puede lograr con ellos."""
 
    num_list=[num1, num2, num3, num4]

    mayorprod = None

    for i in range(4):
        for h in range(i+1,4):
            producto=num_list[i]*num_list[h]
            if mayorprod is None or producto > mayorprod:
                mayorprod = producto
    
    return mayorprod

#print(mayorproducto(1, 5, -2, -4))