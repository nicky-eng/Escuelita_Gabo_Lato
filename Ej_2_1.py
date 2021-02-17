def capital_final(capital, interes, anios):
    """Calcular el capital final dado el capital inicial, tasa de interés de 0 a 100 % y años"""
    capital_fin=capital*(1+interes/100)**anios
    return capital_fin