

def contrasena_correcta(password):
    """Función que verifica si la contraseña ingresada es correcta y devuelve True o False.
    La contraseña debe estar guardad en una variable global llamada 'contraseña'"""

    pass_guardado =  globals(contraseña)
    password_aceptado = (password == pass_guardado)

    return (password_aceptado)
