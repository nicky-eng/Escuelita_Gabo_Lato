"""
Ejercicio 12.4. Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:

>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
>>> c = Caja({500: 6, 100: 7, 2: 4})
>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
>>> c.agregar({50: 2, 2: 1})
>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
>>> c.quitar({50: 2, 100: 1})
200
>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'
"""

class Cashbox:
    """
    Cashbox class that allows 1, 2 ,5, 10, 20, 50,
    100, 200, 500, and 1000 currency bills in it.
    """

    def validate_bill(value):
        "Validates that the note entered valid bill."
        if value not in (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000):
            raise ValueError(f'"{value}" is not a valid note.')
        return value
        
    def validate_amount(amount):
        "Validates that the note entered valid bill."
        if  not isinstance(amount, int) or amount < 0:
            raise ValueError(f'"{amount}" is not a valid amount of bills.')
        return amount

   
    def __init__(self, bills):
        self.notes = dict()
        for bill in bills:
            self.notes[Cashbox.validate_bill(bill)] = Cashbox.validate_amount(bills[bill])

    def __str__(self):

        total = 0
        for bill in self.notes:
            total +=  self.notes[bill]*bill

        return(f'Chashbox {self.notes} total: {total} dollars')

    
    def add_notes(self, bills):
        "Adds the notes in bills to the cashbox."
        for bill in bills:
            self.notes[Cashbox.validate_bill(bill)] = self.notes.get(bill, 0) + Cashbox.validate_amount(bills[bill])
        return self

    def draw_notes(self, bills):
        "Subtracts the notes in bills from the cashbox."
        total_draw = 0
        for bill in bills:
            if self.notes[Cashbox.validate_bill(bill)] < Cashbox.validate_amount(bills[bill]):
                raise ValueError(f'There are not enough "{bills[bill]}" bills to draw.')
            else:
                self.notes[bill] += - bills[bill]
                total_draw += bill * bills[bill]
        print(total_draw)
        return self    