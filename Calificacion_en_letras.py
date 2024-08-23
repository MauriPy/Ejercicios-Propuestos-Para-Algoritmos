# 11) Calificación en letras: Desarrolla un algoritmo que tome una calificación numérica (por ejemplo, de 0 a 100) 
# ingresada por el usuario y la convierta en una calificación en letras (A, B, C, D, E) según un sistema de calificación específico.

# Para este programa pensemos en una calificacion de notas donde A es el 100%, B es 80%, C es 60%, D es 40%, E es 20%.
# para obtener la calificacion lo unico que se hizo fue tomar el total y dividirlo en las letras (5), es decir 100/5=20.
# Entonces por cada 20 puntos tenemos una nota.

# Funcion para calcular la calificacion y retornar la letra.
def Calificacion_letras(calificacion):
    # Calcularemos la letra correspondiente para el numero ingresado.
    # Condicional para la letra E.
    # Este if verifica si la calificacion sea menor o igual a 20, es ese caso le da nota E.
    if calificacion <= 20:
        print(f'La calificaion numerica es: {calificacion}')
        print(f'La calificacion en letra es: E')
        print(f'El porcentaje es del : {calificacion}%')
    
    # Condicional para la letra D.
    # Este if verifica si la calificacion sea mayor a 20 y menor o igual a 40, es ese caso le da nota D.
    elif calificacion > 20 and calificacion <= 40:
        print(f'La calificaion numerica es: {calificacion}')
        print(f'La calificacion en letra es: D')
        print(f'El porcentaje es del : {calificacion}%')

    # Condicional para la letra C.
    # Este if verifica si la calificacion sea mayor a 40 y menor o igual a 60, es ese caso le da nota C.
    elif calificacion > 40 and calificacion <= 60:
        print(f'La calificaion numerica es: {calificacion}')
        print(f'La calificacion en letra es: C')
        print(f'El porcentaje es del : {calificacion}%')

    # Condicional para la letra B.
    # Este if verifica si la calificacion sea mayor a 60 y menor o igual a 80, es ese caso le da nota B.
    elif calificacion > 60 and calificacion <= 80:
        print(f'La calificaion numerica es: {calificacion}')
        print(f'La calificacion en letra es: B')
        print(f'El porcentaje es del : {calificacion}%')

    # Condicional para la letra A.
    # Este if verifica si la calificacion sea mayor a 80 y menor o igual a 100, es ese caso le da nota A.
    elif calificacion > 80 and calificacion <= 100:
        print(f'La calificaion numerica es: {calificacion}')
        print(f'La calificacion en letra es: A')
        print(f'El porcentaje es del : {calificacion}%')

    # En cualquier otro caso.
    else:
        print('La calificacion no cumple los requisitos para ser calculada.')


# Funcion main
def main():
    # Pedimos al usuario que ingrese una calificaion numerica del 1 al 100.
    calificacion = int(input('Ingrese un numero entre 0 a 100: '))

    # Llamada a la funcion.
    Calificacion_letras(calificacion)

# Ejecutador.
if __name__=='__main__':
    main()