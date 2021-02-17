def esbisiesto(anio):
    """Calcula si un año es bisiesto o no. Devuelve True o False si no es bisiesto """

    anio = int(anio)

    if anio % 4 == 0:
        if anio % 100 ==0:
            if anio % 400 == 0:
                dato = True
            else:
                dato = False
        else:
            dato = True
    else:
        dato = False
    
    return dato

def diasenmes(mes, anio):
    """Devuelve la cantidad de días del mes dado un mes y un año específico. No verifica si el mes ingresado es válido"""
  
    mes = int(mes)
    anio = int(anio)

    if mes <= 7: #Porque a partir del mes 8, el pratrón de días cambia.
        if mes == 2:
            bis = esbisiesto(anio)
            if bis == "Es bisiesto.":
                dias = 29
            else:
                dias = 28
        elif mes % 2 == 0:
            dias = 30
        else:
            dias = 31
    else:
        if mes > 12:
            print("El mes ingresado no es válido.")
            dias = 0
        elif mes % 2 == 0:
            dias = 31
        else:
            dias = 30

    return dias

def fechaesvalida(dia, mes, anio):
    """Función que determina si una fecha ingresada es una fecha válida.
           Devuelve True si es válida y False si no lo es."""

    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    esvalida = True

    diasmes = diasenmes(mes, anio)

    if diasenmes == 0:
        esvalida == False
    elif dia > diasmes or dia < 1:
        esvalida = False
        
    return esvalida

def dias_hasta_finde(dia, mes, anio):
    """Devuelve el número de días restantes hasta fin de mes"""

    esvalida = fechaesvalida(dia, mes, anio)

    if esvalida == False:
        print("La fecha ingresada no es válida")
        dias_restantes = None
    else:
        dias_del_mes = diasenmes(mes,anio)
        dias_restantes = dias_del_mes - dia

    return dias_restantes   
    

def dias_transcurridos(dia, mes, anio):
    """Devuelve los días trancsurridos hasta la fecha ingresada."""

    esvalida = fechaesvalida(dia, mes, anio)
    
    dias_bisiesto = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    dias_no_bisiesto = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    dias = 0

    if esvalida == False:
        print("La fecha ingresada no es válida")
        dias = None
    
    elif esbisiesto(anio) == True:
        for i in range(mes - 1):
            dias = dias + dias_bisiesto[i]

        dias = dias + dia - 1 

    else:
        for i in range(mes - 1):
            dias = dias + dias_no_bisiesto[i]
        
        dias = dias + dia - 1
    
    return dias

def dias_hasta_finde_anio(dia, mes, anio):
    """Devuelve la cantidad de días que faltan hasta que se termine el año incluyendo el día de la fecha."""

    esvalida = fechaesvalida(dia, mes, anio)
    
    if esvalida == False:
        print("La fecha ingresada no es válida")
        dias = None

    elif esbisiesto(anio) == True:
        dias = 366 - dias_transcurridos(dia, mes, anio)
    
    else:
        dias = 365 - dias_transcurridos(dia, mes, anio)

    return dias

def tiempo_entre_fechas (dia1, mes1, año1, dia2, mes2, año2):
    """Devuelve el tiempo transcurrido entre las dos fechas en años, meses y días sin importar el 
    orden en que se ingresen las fechas."""
    
    valida1 = fechaesvalida(dia1, mes1, año1)
    valida2 = fechaesvalida(dia2, mes2, año2)
    if valida1 == False or valida2 == False:
        return (print("Al menos una de las fechas ingresadas no es válida."))

    # Determinación de cual es la fecha más grande. Vamos a restar la fecha_b a la fecha_a.

    if año1 > año2:
        dia_a = dia1
        mes_a = mes1
        año_a = año1
        dia_b = dia2
        mes_b = mes2
        año_b = año2

    elif año1 < año2:
        dia_a = dia2
        mes_a = mes2
        año_a = año2
        dia_b = dia1
        mes_b = mes1
        año_b = año1

    elif año1 == año2:
        if mes1 > mes2:
            dia_a = dia1
            mes_a = mes1
            año_a = año1
            dia_b = dia2
            mes_b = mes2
            año_b = año2

        elif mes1 < mes2:
            dia_a = dia2
            mes_a = mes2
            año_a = año2
            dia_b = dia1
            mes_b = mes1
            año_b = año1

        else:
            años = 0
            meses = 0
            dias = abs(dia1 - dia2) # Si el año y el mes son el mismo, la única diferencia está en los días.

            return (años, meses, dias)
    
    if dia_a < dia_b:
        dia_a = dia_a + diasenmes(mes_a, año_a)
        mes_a = mes_a - 1
        dias = dia_a - dia_b
    else:
        dias = dia_a - dia_b
    
    if mes_a < mes_b:
        mes_a = mes_a + 12
        año_a = año_a - 1
        meses = mes_a - mes_b
    else:
        meses = mes_a - mes_b
    
    años = año_a - año_b

    return (años, meses, dias)




    



