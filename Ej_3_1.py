
def calcseg(horas, minutos, segundos):
    """Devuelve el tiempo en segundos, cuando se le da el tiempo en [horas, minutos, segundos]."""  
    return int(horas * 3600 + minutos * 60 + segundos)


def calctiempo(segundos):
    """Devuelve el tiempo en [horas, minutos, segundos] cuando se le da un tiempo total en segundos."""
    horas=int(segundos//3600)
    minutos= int((segundos % 3600) // 60)
    segresto=int((segundos % 3600) % 60)

    return [horas, minutos, segresto]