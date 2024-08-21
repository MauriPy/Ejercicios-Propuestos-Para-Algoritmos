# 6) Ordenamiento: Crea un algoritmo que ordene un conjunto de números ingresados por el usuario en orden ascendente o descendente.
# Funciones metodo burbuja.

# Existen varios metodos de ordenamiento, burbuja, sort, etc.
    # En este caso usare el metodo burbuja ya que ayuda a entender la logica de la programacion de mejor manera.
    # Metodo burbuja.
    # Este metodo consiste en recorrer el arreglo y comparar 2 posiciones e intercambiar el numero ya sea mayor o menor.
    # e ir intercambiando las posiciones.

# Funcion de metodo burbuja ascendente.
def MetodoburbujaA(numeros):
    # Este for es para hacer las pasadas por la lista para todas las comparaciones.
    for i in range(0,len(numeros) - 1):
        # Este for es para hacer las comparaciones e ir intercambiando.
        for j in range(0, len(numeros) - i - 1):
            # El if pregunta al programa, el numero es mayor al siguiente?, 
            # en caso verdadero el numero actual se intercambia al siguiente.
            # en caso contrario se mantiene la posicion.
            if numeros[j] > numeros[j + 1]:
                # Este auxiliar es para guardar el valor del primer numero.
                aux = numeros[j]
                # Aqui ocurre el intercambio.
                numeros[j ] = numeros[j + 1]
                # Aqui el auxiliar avanza 1 puesto.
                numeros[j + 1] =  aux
    return numeros
    
# Funcion de metodo burbuja descendente.
def MetodoburbujaD(numeros):
    # Este for es para hacer las pasadas por la lista para todas las comparaciones.
    for i in range(0,len(numeros) - 1):
        # Este for es para hacer las comparaciones e ir intercambiando.
        for j in range(0, len(numeros) - 1):
            # El if pregunta al programa, el numero es menor al siguiente?, 
            # en caso verdadero se mantiene la posicion.
            # en caso contrario se intercambian las posiciones.
            if numeros[j] < numeros[j + 1]:
                # Este auxiliar es para guardar el valor del primer numero.
                aux = numeros[j]
                # Aqui ocurre el intercambio.
                numeros[j ] = numeros[j + 1]
                # Aqui el auxiliar avanza 1 puesto.
                numeros[j + 1] =  aux
    return numeros

# Funcion main para pedir datos al usuario.
def main():
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
            # Agregamos lo ingresado por el usuario, convertimos a float el string para que funciones bien la comparacion en el metodo burbuja.
            numeros.append(float(n))

    # Mostramos la lista de los numeros original.
    print(f'\nLa lista de numeros original es: {numeros}')

    # Preguntamos al usuario que metodo quiere usar si ascendente o descendente.
    opcion = input('Ingrese la letra A(Ascendente) o D(Descendente): ')

    # Aqui evaluamos la opcion escogida por el cliente y segun eso llamamos al metodo correspondiente.
    if opcion.lower() == 'a' :
        MetodoburbujaA(numeros)
        # Mostramos la lista ordenada final de forma ascendente.
        print(f'La lista ordenada de forma ascendente es: {numeros}')
    elif opcion.lower() == 'd':
        MetodoburbujaD(numeros)
        # Mostramos la lista ordenada final de forma Descendente.
        print(f'La lista ordenada de forma descendente es: {numeros}')
    else:
        # En caso que ingrese otra letra se termina el programa y le informa el error.
        print('Ingresaste una letra que no es valida...')

    
if __name__ == '__main__':
    main()


