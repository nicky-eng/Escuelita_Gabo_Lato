"""
Ejercicio 12.1.
a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta.
b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo 
resultante de la intersección entre ambos, o lanzar una excepción si la intersección
es nula.
d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes 
ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo intervalo 
resultante de la unión entre ambos.
"""

class Interval:
    """
    Representation of a time interval between two points in time given in seconds.
    """

    def validate_integer(value):
        "If value is an integer it returns that value, if it is not, it raises a TypeError."
        if not isinstance(value, int):
            raise TypeError("{} is not an integer".format(value))
        return value

    def __init__(self, time1, time2):
                
        self.time1 = Interval.validate_integer(time1)
        self.time2 = Interval.validate_integer(time2)
        assert time2 > time1, "Time 2 must be bigger than Time 1"
    
    def __str__(self):
        """Converts to string."""        
        return "({}, {})".format(self.time1, self.time2)

    def time_interval(self):
        """Returns the length of time in the interval."""        
        return int(self.time2 - self.time1)
    
    def intersection(self, other):
        """
        Returns a new interval of the intersection of both, or
        raises an exception if intersection is null.
        """
        #if other.time2 <= self.time1 or other.time1 >= self.time2:
         #   raise ValueError("Intervals {} and {} have no intersection".format(self, other))

        try:

            if other.time1 >= self.time1:
                intersection_begin = other.time1
                if other.time2 <=self.time2:
                    intersection_end = other.time2
                else:
                    intersection_end = self.time2
            else:
                intersection_begin = self.time1
                if other.time2 < self.time2:
                    intersection_end = other.time2
                else:
                    intersection_end = self.time2
            return Interval(intersection_begin, intersection_end)

        except: print(ValueError("Intervals {} and {} have no intersection".format(self, other)))

    def union(self, other):
        """"Returns a new interval composed by the union of both, or raises an exception
        if they are not adjacent.
        """
        if other.time2 < self.time1 or other.time1 > self.time2:
            raise ValueError("Intervals {} and {} are not adjacent or do not intersect.".format(self, other))

        if other.time1 <= self.time1:
            union_begin = other.time1
        else:
            union_begin = self.time1
        if other.time2 >= self.time2:
            union_end = other.time2
        else:
            union_end = self.time2
        return Interval(union_begin, union_end)




  
p = Interval(28, 34)
p2 = Interval(34, 390)
print(p)

w = p.time_interval()
w2 = p2.time_interval()
print(w)

new = p.intersection(p2)
print("Intersection:", new)
union = p.union(p2)
print("Union: ", union)
