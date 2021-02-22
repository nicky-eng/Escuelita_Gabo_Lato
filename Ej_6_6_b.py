def reemplazo_vocales_sin_dic(cadena):
    """Función que reemplaza cada vocal por su próxima vocal sin usar diccionarios"""
       
    reemplazos = ['u', 'o', 'i', 'e', 'a']
    nueva_cadena = ''
    for i in cadena:
        if i in reemplazos:
            reemplazos.index(i)
            nueva_cadena = nueva_cadena + reemplazos[reemplazos.index(i)-1]
        else:
            nueva_cadena = nueva_cadena + i
    
    return nueva_cadena

#vistaeroueee
#string = 'vestuarioeee'
#print(reemplazo_vocales_sin_dic(string))
