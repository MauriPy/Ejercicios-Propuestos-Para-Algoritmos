# 8) Contador de palabras: Escribe un algoritmo que cuente el número de palabras en una cadena de texto ingresada por el usuario.

# Para contar palabras en python podemos usar el comando reservado split().
# Split divide cadenas de texto segun el delimitador que le pasemos y lo guarda en una lista donde cada posicion es una palabra.
# Ej:
# Frase ingresadas: hola como estas
# Frase con split():  ['hola', 'como', 'estas']

# Pedimos al usuario ingresar una frase cualquiera.
frase = input('Ingrese una frase u oracion para contar las palabras: ')
# Mostramos la frase original.

# Una vez ingresada la frase u oracion, debemos hacer el split a esa variable.
# Asi split() nos entregara una lista nueva con las palabras de la frase ingresada.

# Definimos la variable para el split().
# El split tiene como delimitador por defecto el ' ', que serian los espacios en blanco
frase_split = frase.split()
print(f'Palabras obtenidas {frase_split}')

# Para el numero de palabras, solo debemos obtener el largo de la lista palabras con len.
palabras = len(frase_split)

# Mostramos en pantalla el total de palabras obtenidas de la frase.
print(f'El total de palabras contadas fueron de: {palabras}')