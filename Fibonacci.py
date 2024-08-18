# 4) Fibonacci: Escribe un algoritmo que genere la secuencia de Fibonacci hasta un número dado por el usuario.
'''
La sucesión de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores, 
comenzando con 0 y 1
'''

# Pedimos al usuario que ingrese un numero.
n = int(input('Ingrese un numero: '))

# Calculamos la serie de fibonacci, con una funcion la cual sume todos los numeros.
# En el caso que sea 0, devolver 0.
# En el caso de ser 1, devolver 1.
# En el caso de que el numero ingresado no sea ni 0 ni 1, se deben sumar todos los numeros anteriores hasta el que ingreso el usuario.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Mostramos en pantalla el resultado de la sucesion.
print(f'La sucecion de fibonacci hasta el numero {n}, es: {fibonacci(n)}')
