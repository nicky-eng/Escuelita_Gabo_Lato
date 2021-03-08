"""
Ejercicio 12.2.
a) Crear una clase Fraccion, que cuente con dos atributos: numeratoro y denominator, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.
b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
con la suma de ambas.
c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
con el producto de ambas.
d) Crear un método simplificar que modifica la fracción actual de forma que los valores
del numeratoro y denominator sean los menores posibles.
"""

class Fraction:
    """Represents a fractional number."""

    def validate_input(value):
        "Validates that value is an integer."
        if not isinstance(value, int):
            raise TypeError("{} is not an integer.".format(value))
        return value
    
    def __init__(self, numerator, denominator):
        "Constructor of Fraction. numerator and denominator must be numerical."
        
        self.numerator = Fraction.validate_input(numerator)
        self.denominator = Fraction.validate_input (denominator)

    def __str__(self):
        "Returns the representation of Fraction as string x/y."
        if self.denominator != 1:
            return "{}/{}".format(self.numerator, self.denominator)
        else:
            return "{}".format(self.numerator)
    
    def __add__(self, other):
        "Implements the add method for the fractions."
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        
        #We use the Euclidian Algorithm to find the minimun common denominator
        m = new_denominator
        n = new_numerator

        if m >= n: 
            r = m % n
            while r != 0:
                m = n
                n = r
                r = m % n
        else:
            m, n = n, m
            r = m % n
            while r != 0:
                m = n
                n = r
                r = m % n

        new_denominator = int(new_denominator / n)
        new_numerator = int(new_numerator / n)

        return Fraction.simplify(Fraction(new_numerator, new_denominator))
    
    def __mul__(self, other):
        "Implements the multiplication method."
        new_nominator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction.simplify(Fraction(new_nominator, new_denominator))
    
    def simplify(self):
        "Simplifies the numerator and the denominator."
            #We use the Euclidian Algorithm to find the minimun common denominator
        m = self.numerator
        n = self.denominator

        if m >= n: 
            r = m % n
            while r != 0:
                m = n
                n = r
                r = m % n
        else:
            m, n = n, m
            r = m % n
            while r != 0:
                m = n
                n = r
                r = m % n

        new_denominator = int(self.denominator / n)
        new_numerator = int(self.numerator / n)

        return Fraction(new_numerator, new_denominator)



a = Fraction(33, 54)
print(a)

b = Fraction(8, 9)
print(a + b)

print(a * b)

print(Fraction.simplify(a))


        