"""
Ejercicio 8.4. Sistema de facturación simplificado
Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identificador,
descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste en una tupla 
de (identificador, cantidad). Se desea generar una factura que incluya la cantidad, la descripción, el 
precio unitario y el precio total de cada producto comprado, y al final imprima el total general.
Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.
"""

def item_invoice_system(products, items):
   
    """
    Prints a receipt with the quantity, description, unit price and total price for
    each item and the total amount of the purchase.

            Parameters:
                    products [(item_code, description, price),] (list of tuples): A list of tuples
                    with the item code, description and price.
                    items [(item_code, amount),] (list of tuples): A list of tuples with the item 
                    code and the amount of items bought.

            Returns:
                    receipt [(amount, description, unit_price, item_total), ..., (total)]: A list with 
                    tuples with quantity, description, unit price and total price for each item and the
                    total amount of the purchase.
                    print(receipt): It prints the receipt to screen.
    """

    item_total = 0
    total = 0
    receipt = []
    products_dictionary = {}

    for product in products:
        products_dictionary[product[0]] = [product[1], product[2]]

    for item in items:
        item_total = (item[1]) * (products_dictionary[item[0]][1])
        receipt.append((item[1], products_dictionary[item[0]][0], products_dictionary[item[0]][1], item_total))
        total = total + item_total
    receipt.append((total,))

    print(receipt)
    return receipt

        


