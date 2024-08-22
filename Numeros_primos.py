# 10) Números primos: Crea un algoritmo que determine si un número ingresado por el usuario es primo o no.

# Para saber ni un numero n es primo tenemos que:
# Debe ser un numero entero y positivo.
# Si n (numero) es divisible por 1 y por si mismo.
# Si el numero ingresado es menor o igual a 1 No es primo.
# En cualquier otro caso el numero No es primo.
# Debe ser un numero entero.

# Pedimos al usuario que ingrese un numero entero positivo.
n = input(f'Ingrese un numero :')

#Primero crearemos las condicionales para verificar que cumpla todas y saber si es primo.
# Debe ser un numero entero y positivo.
if n.is_integer():
    print('Es entero')
else:
    print('No es un numero primo')