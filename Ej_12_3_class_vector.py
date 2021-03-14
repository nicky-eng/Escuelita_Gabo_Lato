"""
Ejercicio 12.3.
a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
misma cantidad de elementos debe levantar una excepción.
c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
los elementos multiplicados por ese número.
"""
from validate_number import validate_number
class Vector:
    """Representation of a vector in 2 or 3 dimensional space."""


    def __init__(self, coordinates):
        "Vector constructor, coordinates must be a list of numbers."

        if len(coordinates) == 2:
            self.x = validate_number(coordinates[0])
            self.y = validate_number(coordinates[1])
        else:
            self.x = validate_number(coordinates[0])
            self.y = validate_number(coordinates[1])
            self.z = validate_number(coordinates[2])

    
    def __len__(self):
        "Returns the length of the vector."
        return len(self.__dict__)


    def __str__(self):
        "Converts to string."
        if len(self) == 2:
            return f"[{self.x},{self.y}]"
        else:
            return f"[{self.x},{self.y},{self.z}]"
    

    def __add__(self, other):
        "Returns a new vector, with the sum of both."
        if len(self) != len(other):
            raise Exception('Vectors are not the same length.')
        else:
            if len(self) == 2:
                return Vector([self.x + other.x, self.y + other.y])
            else:
                return Vector([self.x + other.x, self.y + other.y, self.z + other.z])
    
    def __mul__(self, multiplier):
        "Returns the scalar product of the vector."
        if len(self) == 2:
            return Vector([self.x * multiplier, self.y * multiplier])
        else:
            return Vector([self.x * multiplier, self.y * multiplier, self.z * multiplier])


coordinates = [3, 4, 3]
v2 = [2, 5]


my_vector = Vector(coordinates)
myv2 = Vector(v2)
er = my_vector.__dir__()
for i in er:
    print(i)

#print(dir(my_vector))
#for i in my_vector:
 #   print(i)
#print(my_vector + myv2)
print(len(my_vector))
print(my_vector)
print(my_vector * 2)
print(myv2 * 2)

    
