# 5) Mayor de tres números: Diseña un algoritmo que determine cuál de tres números ingresados por el usuario es el mayor.
# la forma mas logica de hacer el calculo para saber cual numero es mayor que otro en una lista, seria comparando los numeros 
# de la lista entre si y agregando a una lista, luego recorrer la lista e ir clasificando el numero que entra si es mayor agregarlo 
# en caso de ser menor mantener la variables como esta.

# Pedimos al usuario que ingrese los 3 numeros y estos deben agregarse a una lista vacia.
# Definimos la lista vacia para almacenar los numeros.
numeros = []

# Creamos el ciclo para preguntar los numeros y agregarlos a la lista.
for i in range(0,3):
    n = int(input(f'Ingrese el numero {i+1}: '))

    # Agregamos los numeros a la lista.
    numeros.append(n)

# Definimos una variable vacia, que sera el numero mayor cada vez que se actualice.
# Variable vacia numero mayor.
n_mayor = numeros[0]

# Evaluamos si el numero es mayor al primero de en la lista numeros.
# En caso de ser verdad la variable n_mayor se actualiza, en caso contrario se mantiene.
for numero in numeros:
    if numero > n_mayor:
        n_mayor = numero

# Mostramos la lista con los numeros agregados.
print(f'Los numeros agregados son: \n {numeros}')

# Mostramos el numero mayor obtenido de la lista.
print(f'El numero mayor de la lista es: {n_mayor}')

