# 14) Calculadora: Crea un algoritmo que funcione como una calculadora básica, 
# capaz de realizar operaciones de suma, resta, multiplicación y división con dos números ingresados por el usuario.

# Funciones de la calculadora.
# Sumar.
def sumar(num1, num2):
    # Sumamos los numeros.
    suma = num1 + num2
    # Mostramos el resultado.
    print(f'La suma de {num1} + {num2} es: {suma}')

# Restar.
def restar(num1, num2):
    # Restamos los numeros.
    resta = num1 - num2
    # Mostramos el resultado.
    print(f'La resta de {num1} - {num2} es: {resta}')

# Multiplicar.
def multiplicar(num1, num2):
    # Multiplicamos los numeros.
    multiplicacion = num1 * num2
    # Mostramos el resultado.
    print(f'La multiplicacion de {num1} * {num2} es: {multiplicacion}')

# Dividir.
def dividir(num1, num2):
    # Dividimos los numeros.
    division = num1 / num2
    # Mostramos el resultado.
    print(f'La division de {num1} / {num2} es: {division}')

# Funcion main.
def main():
    # Pedimos al usuario que ingrese sus 2 numeros.
    num1 = float(input('Ingrese el numero 1: '))
    num2 = float(input('Ingrese el numero 2: '))

    print('='* 30)
    print('|        Calculadora         |')
    print('='* 30)

    # Crearemos un while para preguntar al usuario que quiere hacer hasta que elija la opcion de salir de la calculadora.
    # Creamos una variable para que el bucle while sigua o no.
    seguir = True

    # El while mientras la variable seguir sea True no se terminara.
    while(seguir):
        print('\nElija la opcion que desea realizar: \n')
        opcion = int(input('1) Sumar.\n2) Restar.\n3) Multiplicar.\n4) Dividir.\n5) Salir.\nIngrese la opcion: '))

        # Creamos un condicional para cada opcion del menu.
        if opcion == 1:
            # Llamamos a la funcion para sumar los numeros.
            sumar(num1, num2) 
        elif opcion == 2:
            restar(num1, num2)
        elif opcion == 3:
            multiplicar(num1, num2)
        elif opcion == 4:
            dividir(num1, num2)
        else:
            print('Saliendo de la calculadora...')
            seguir = False

if __name__ == '__main__':
    main()