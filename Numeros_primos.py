# 10) Números primos: Crea un algoritmo que determine si un número ingresado por el usuario es primo o no.

# Para saber ni un numero n es primo tenemos que:
# 1) Debe ser un numero entero y positivo mayor a 1.
# 2) Si el numero es divisible por 1 y por si mismo.
# 3) En cualquier otro caso el numero No es primo.

#Primero crearemos las condicionales para verificar que cumpla todas y saber si es primo.
# Debe ser un numero entero y positivo mayor a 1.
# Funcion para saber si es primo.
def Esprimo(n):
    # Buscamos los factores de n y si en un factor (%) el resultado es 0 ya no es primo.
    # Cualquier otro resultado, no es primo.
    for i in range(2, n):
        # Este if compara el numero n y lo divide por i que va desde 2 hasta n, por ende.
        # Como sabemos un numero primo debe ser divisible por 1 y por si mismo.
        # Todo numero siempre es divisible por si mismo, esto es siempre verdad por lo que no debemos verificarlo.
        # Verificamos entonces que el numero sea divisible SOLO por 1.
        # Un numero es divisible por 1 cuando su resto es 0.
        # El if lo que verifica es exactamente eso, al dividir cada numero por el numero n, si en algun momento el resto es 0,
        # Quiere decir que el numero no es primo ya que seria divisible por un numero que no es el mismo.
        # El bucle recorre desde 2 hasta n-1, es decir no incluye a si mismo.
        if n % i == 0:
            print('No es primo')
            
            return False
    print('Si es primo')
    return True

# Funcion main.
def main():
    # Pedimos al usuario que ingrese un numero entero positivo.
    n = float(input(f'Ingrese un numero : '))

    # ver si es un numero entero mayor a 1.
    if n > 1:
        # En caso de cumplirse convertimos el numero a entero y verificamos si es primo llamando a la funcion Esprimo.
        n = int(n)
        # Llamada a la funcion para saber si es primo o no.
        Esprimo(n)
    else:
        # Si el numero no es mayor a 1, 
        print('No es un numero positivo o mayor a 1')

if __name__ == '__main__':
    main()
