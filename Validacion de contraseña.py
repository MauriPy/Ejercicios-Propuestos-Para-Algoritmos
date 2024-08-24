# 13) Validación de contraseña: Diseña un algoritmo que valide si una contraseña ingresada por el usuario cumple con ciertos requisitos 
# de seguridad, como longitud mínima, uso de mayúsculas, minúsculas y números.

# Importamos la libreria string (Libreria que contiene verificacion para caracteres especiales comunes).
# Importamos la libreria getpass para el input del inicio y que no muestre la contraseña ingresada.
import string, getpass

# Funcion que verifica la longitud mínima (que la longitud no sea menor a 8 caracteres.)
def largoPassword(password):
    largo_password = len(password)

    # 1) Condicion que verifica que al menos tenga 8 numeros en la constraseña.
    if largo_password >= 8:
        print('Si cumple el primer requisito de tener al menos 8 caracteres')

        # Retornamos true para que al validar sepa que se cumplio este requisito.
        return True

    # En caso contrario no cumple el requisito.
    else:
        print('La constraseña debe tener al menos 8 caracteres.') 
        return False  

# Funcion que verifica el uso de mayúsculas (que tenga almenos 1 mayuscula y 1 minuscula)
def MayusAndMinusPassword(password):
    # Para verificar que la password tenga al menos 1 mayuscula y 1 minuscula.
    # Debemos recorrer la password con un for y verificar que tenga 1 letra mayuscula y 1 minuscula.
    # Para contar las mayusculas y minusculas definimos 2 contadores.

    # Contador de mayusculas.
    cont_mayus = 0

    # Contador de minusculas.
    cont_minus = 0

    # Este for recorre desde el primer caracter hasta el ultimo de la password.
    for i in range(0, len(password)):
        # Este print muestra cada caracter de las password ingresada de a 1.
        #print(password[i])
        # Verificamos que al menos 1 caracter sea minuscula para decir que esta bien.
        if password[i].islower():
            # Muestra los caracteres minusculas.
            #print(f'{password[i]} Es minuscula ')
            # Suma 1 al contador de minus.
            cont_minus += 1
        else:
            # Muestra los caracteres mayusculas.
            #print(f'{password[i]} Es mayuscula ')
            # Suma 1 al contador de mayus.
            cont_mayus += 1

    #  Verificacion de que las mayus y minus sean al menos 1. 
    if cont_mayus >= 1 and cont_minus >= 1:
        print('Si cumple el requisito porque tiene al menos 1 mayuscula y 1 minuscula')
        return True
    else:
        print('No cumple los requisitos de mayusculas y minusculas...')
        return False

    # Mostramos en pantalla el contador de mayus y minus.
    #print(cont_mayus)
    #print(cont_minus)

# Funcion que verifica que la contraseña tenga al menos 1 numero.
def NumeroPassword(password):
    # Para verificar que la contraseña tenga un numero al menos.
    # Debemos recorrer la password y contar al menos 1 numero.
    cont_num = 0
    # Este for recorre desde el primer caracter hasta el ultimo de la password y cuenta los numeros si tiene.
    for i in range(0, len(password)):
        if password[i].isdigit():
            #print(f'{password[i]} Es numero ')
            cont_num += 1

    #  Verificacion de que haya almenos 1 numero en la contraseña. 
    if cont_num >= 1:
        print('Si cumple el requisito porque tiene al menos 1 numero')
        return True
    else:
        print('No cumple el requisito ya que la contraseña debe tener al menos 1 numero...')
        return False

# Funcion que verifica que tenga al menos 1 caracter especial (!@#$%^).
def CaracterEspecialPassword(password):
    # Para verificar que la contraseña tenga un caracter especial.
    # Debemos recorrer la password y ver con string.punctuation si tiene algun caracter especial.
    # Si es verdad quiere decir que tiene al menos 1 caracter especial.
    # En caso contrario no tendra caracteres especiales.

    # Verificamos que tenga al menos 1 caracter especial la password.
    # Este for recorre caracter por caracter y el if verifica si cumple con ser especial.
    for i in range(0,len(password)):
        if password[i] in string.punctuation:
            # En caso de cumplirse, sabemos que tiene al menos 1 caracter especial y retornamos true.
            print('Si cumple el requisito al tener al menos 1 caracter especial...')
            return True
        
    # En caso contrario no cumple y retornamos false.
    print('No cumple el requisito al no tener caracteres especiales...')
    return False

# Funcion para verificar que la contraseña cumpla con todos los requisitos.
def validar(password):
    # Esta funcion sera la encargada de verificar todos los anteriores requisitos.
    # Verificamos que todas las funciones se cumplan al mismo tiempo.
    if largoPassword(password) and MayusAndMinusPassword(password) and NumeroPassword(password) and CaracterEspecialPassword(password):
        print('\nLa contraseña SI cumple con todos los requisitos necesarios')
    else:
        print('\nLa contraseña NO cumple con todos los requisitos...')


# Funcion main.
def main():
    # Primero le pedimos al usuario que ingrese una constraseña.
    # Como es una contraseña, para hacerlo mas realista utilizaremos la libreria getpass que oculta el ingreso de la contraseña.
    password = getpass.getpass('Introduzca una contraseña: ')

    print('Contraseña ingresada con exito..\n')
    print('Validando....')

    # Como nos piden que todos los requisitos se cumplan.
    # Al crear 1 funcion para cada requisito es mas facil validar.
    # Llamamos a la funcion que validara la password y todos los requisitos.
    validar(password)

if __name__ == '__main__':
    main()