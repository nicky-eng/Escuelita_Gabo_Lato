def insertar_carcater(cadena, separador):
    """Para una cadena dada, inserta el separador entre cada una de las letras de esa cadena."""
    nueva_cadena = ()
    for i in (cadena):
        agregar = cadena[i] + separador
        nueva_cadena = nueva_cadena + agregar
    
    return nueva_cadena
