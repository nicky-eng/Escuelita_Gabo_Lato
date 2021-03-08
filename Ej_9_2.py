def dic_contar_palabras(cadena):
    """Arma un diccionario con contadores de palabras de cada uno de las apariciones
    de la cadena entregada."""

    dic = {}
    palabra_aux = '' 
    cadena = cadena.lower()
    abc = 'abcdefghijklmnopqrstuvwxyzáéíóú '

    for i in cadena:
        if i in abc:
            if i == ' ':
                if palabra_aux in dic:
                    dic[palabra_aux] += 1
                    palabra_aux = ''
                else:
                    dic[palabra_aux] = 1
                    palabra_aux = ''
            else:
                palabra_aux = palabra_aux + i
    if palabra_aux in dic: #Agrego esta última instancia de if, else para que la última palabra guardada en
                           # palabra auxiliar esté incluida en el diccionario.
            dic[palabra_aux] += 1
            palabra_aux = ''
    else:
        dic[palabra_aux] = 1
        palabra_aux = ''
    
    return dic
            
#test = "Qué lindo día que hace hoy. Pero qué vamos a hacer hoy?"
#print(dic_contar_palabras(test))

def dic_contar_caracteres(cadena):
    """Arma un diccionario con contadores de caracteres con cada una de sus apariciones
    en la cadena entregada."""

    dic = {} 
    cadena = cadena.lower()
    abc = 'abcdefghijklmnopqrstuvwxyzáéíóú'

    for i in cadena:
        if i in abc:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    
    return dic
            
#test = "Bananas, ananás y abas"
#print(dic_contar_caracteres(test))

def dic_count_sum_dice(nr_rolls):
    """It recieves a number of times two dice must be rolled and counts de amount of times
    each sum of dice comes up."""

    from dice_roll import dice_roll

    rolls = dice_roll(nr_rolls, 2)

    dic = {}
    for i in rolls:
        if i[0] + i[1] in dic:
            dic [i[0] + i[1]] += 1
        else:
            dic [i[0] + i[1]] = 1

    return dic, rolls

#print(dic_count_sum_dice(8))