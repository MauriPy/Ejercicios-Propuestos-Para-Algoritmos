# 12) Cálculo de interés compuesto: Implementa un algoritmo que calcule el monto final de una inversión con interés compuesto,
# dados el capital inicial, la tasa de interés y el tiempo.

# Primero debemos saber que es el interes compuesto y como se calcula.
# Cf = Ci*(1+i)^n
# Donde:
# 
# Cf = Capital final.    / Cf
# Ci = Capital inicial.  / Ci
# i = Tasa de interes.   / Tasa_i
# n = periodo de ahorro. / Tiempo

# Funcion para calcular el interes compuesto.
# Esta funcion recibe los 3 parametros anteriores ingresados por el usuario.
def Calculo_Interes_C(Ci, tasa_i, tiempo):

    # El interes se maneja en porcentajes, por lo que debemos convertirlo antes de que entre a la formula.
    tasa_i_decimal = tasa_i/100

    # Ponemos la formula.
    Cf = Ci *(1 + tasa_i_decimal)**tiempo

    # Mostramos en pantalla el numero redondeado a 2 decimales con la funcion round().
    print(f'El calculo del interes compuesto es de ${round(Cf, 2)}')

    return Cf


# Funcio main.
def main():
    # Con la formula de interes compuesto, ahora debemos pedir al usuario que ingrese los datos.
    # Datos: capital inicial, tasa de interes, tiempo.
    Ci = float(input('Ingrese el capital inicial: '))
    tasa_i = float(input('Ingrese el capital la tasa de interes: '))
    tiempo = float(input('Ingrese el tiempo en años: '))

    # Llamamos a la funcion para calcular el interes compuesto.
    Calculo_Interes_C(Ci, tasa_i, tiempo)
    
if __name__=="__main__":
    main()
