def plegado_de_texto(texto, n):
    """A partir de un texto determinado, devuelve el texto, segmentado en una lista de
    cadenas de una longitud no mayor que n caracteres incluyendo espacios."""

    texto_plegado =[]
    texto_auxiliar = ''
    palabra_auxiliar = ''

    for i in texto:
        palabra_auxiliar = palabra_auxiliar + i
        if i == ' ':            
            if len(texto_auxiliar) + len (palabra_auxiliar) <= n:
                texto_auxiliar = texto_auxiliar + palabra_auxiliar
                palabra_auxiliar = ''
            else:
                texto_plegado.append(texto_auxiliar)
                texto_auxiliar = ''

    return texto_plegado      
                                          
texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel nulla in ligula semper gravida id at tortor. Curabitur suscipit ante metus, et lacinia augue elementum vel. Curabitur ultrices hendrerit tellus, sit amet auctor nunc. Suspendisse enim ex, pharetra a lorem a, facilisis tincidunt nibh. Nunc in tortor tempus, ornare nibh vel, lobortis libero. Praesent ac nisl elit. Integer suscipit, lectus ut malesuada malesuada, nisi justo rutrum nunc, eu condimentum felis nibh ac dolor. Nulla gravida sem non libero vulputate luctus. Donec dictum purus in ligula venenatis molestie. Praesent scelerisque odio sit amet metus lobortis vestibulum eu ac orci. Quisque tincidunt dignissim sapien non egestas. '
n = 50
print(plegado_de_texto(texto, n))

