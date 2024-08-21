# 7) Promedio: Desarrolla un algoritmo que calcule el promedio de un conjunto de números ingresados por el usuario.

# Funcion para calcular el promedio con una lista de numeros como parametro.
def CalcularPromedio(numeros):
    # Para calcular el promedio en un grupo de numeros.
    # La logica normal seria, sumar todos los numeros y luego dividir el resultado de la suma por el total de numeros.
    
    # Obtendremos primero la suma de todos los numeros de la lista y lo guardamos en una variable llamada total.
    total= sum(numeros)

    # Ahora dividimos el total obtenido por el total de numeros de la lista.
    # Primero obtenemos el total de numeros ingresados a la lista, con la palabra reservada len.
    cant_n = len(numeros)

    # Ahora con el total de la suma, y el total de numeros ingresados, procedemos a dividir para obtener el promedio.
    promedio = total/cant_n

    # Mostramos el promedio en pantalla.
    # Mostramos el promedio obtenido de la lista.
    print(f'El promedio de los numeros ingresados es: {promedio}')
    
    return promedio
    
    


# Funcion main.
def main():
    # Pedimos al usuario ingresar numeros de forma infinita hasta que presione x o X, para terminar.
    # Lista vacia para almacenar todos lo numeros que ingrese el usuario al programa.
    numeros = []

    # El bucle while es para preguntar infinitamente al usuario numeros hasta que ingrese x o X y se termina el ciclo.
    while True:
        # Pedimos al usuario que ingrese numeros.
        n = input('Ingrese numeros (x para no ingresar mas): ')

        # Condicional para saber cuando el usuario terminara de ingresar numeros.
        # Si ingresa x o X el bucle se termina.
        if n == 'x' or n == 'X':
            break

        else:
            # Agregamos lo ingresado por el usuario, convertimos a entero el string para que funciones bien la comparacion en el metodo burbuja.
            numeros.append(float(n)) 

    # Mostramos la lista de los numeros original.
    print(f'\nLa lista de numeros es: {numeros}')

    #Llamamos a la funcion para calcular el promedio.
    CalcularPromedio(numeros)

if __name__ == '__main__':
    main()
