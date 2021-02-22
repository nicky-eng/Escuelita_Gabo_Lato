def vote_por_mi(lista):
    """Función que recibe una tupla de nombres y devuelve el mensaje dirigido a cada nombre."""
    
    for i in lista:
        print("Estimado/a {}, vote por Nicky 2024.".format(i))

#a = ('Nicolas', 'Gaston', 'Magdalena')
#vote_por_mi(a)

def vote_por_mi_rango(lista, p, n):
    """Función que recibe una tupla de nombres y devuelve el mensaje dirigido a cada nombre desde
    la posición 'p' hasta las próximas 'n' personas."""
    
    for i in range(p, p + n):
        print("Estimado/a {}, vote por Nicky 2024.".format(lista[i]))

#a = ('Nicolas', 'Gaston', 'Magdalena', 'Germán', 'Pedro', 'Mabel', 'Matías', 'Margarita', 'Manuela', 'Marta')
#p = 2
#n = 4
#vote_por_mi_rango(a, p, n)

def vote_con_género(lista):
    """Función que recibe una tupla de nombres y devuelve el mensaje dirigido a cada nombre teniendo en
    cuenta el género de la persona donde el género se ingresa como 'F' de femenino o 'M' de masculino."""
    
    for i in lista:
        if i[1] == 'F' or i[1] == 'f':
            print("Estimada {}, vote por Nicky 2024.".format(i[0]))
        elif i[1] == 'M' or i[1] == 'm':
            print("Estimado {}, vote por Nicky 2024.".format(i[0]))
        else:
            print('Resuelva manualmente para {}.'.format(i[0]))

#a = (('Nicolas', 'm'), ('Gaston', 'M'), ('Magdalena', 'F'), ('Tyn', 'b'))
#vote_con_género(a)

def vote_por_mi_rango_con_genero(lista, p, n):
    """Función que recibe una tupla de nombres y devuelve el mensaje dirigido a cada nombre desde
    la posición 'p' hasta las próximas 'n' personas, teniendo en cuenta el género de la persona
    donde el género se ingresa como 'F' de femenino o 'M' de masculino."""
    
    for i in range(p, p + n):
        if lista[i][1] == 'F' or lista[i][1] == 'f':
            print("Estimada {}, vote por Nicky 2024.".format(lista[i][0]))
        elif lista[i][1] == 'M' or lista[i][1] == 'm':
            print("Estimado {}, vote por Nicky 2024.".format(lista[i][0]))
        else:
            print("Resuelva manualmente para {}.".format(lista[i][0]))


#a = (('Nicolas', 'm'), ('Gaston', 'M'), ('Magdalena', 'f'), ('Germán', 'm'), ('Pedro', 'e'), ('Mabel', 'f'), ('Matías', 'p'))
#p = 2
#n = 3
#vote_por_mi_rango_con_genero(a, p, n)