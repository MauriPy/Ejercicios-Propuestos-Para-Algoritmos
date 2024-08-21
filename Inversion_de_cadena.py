# 9) Inversión de cadena: Diseña un algoritmo que invierta una cadena de texto ingresada por el usuario.

# Pedimos al usuario ingresar una cadenas u oracion.
cadena = input('Ingrese una cadena de palabras para invertirla: ')

# En python las palabras son tmb listas.
# Ej:
# Palbra = hola
# Palabra en lista: [h,o,l,a]

# Invertimos la palabra con un slicing (rebanador) de python.
# En este caso utilizaremos el que nos invierte una lista el cual es [::-1].
cadena_invertida = cadena[::-1]

# Mostramos en pantalla la cadena invertida.
print(f'\nLa cadena original era: {cadena}')

# Mostramos en pantalla la cadena invertida.
print(f'La cadena invertida es: {cadena_invertida}')
