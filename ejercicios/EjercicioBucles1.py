#Ejercicio para que escriba un programa que encuentre la mínima secuencia de múltiplos de 3 (distintos) cuya suma sea igual o superior a un valor dadoN= int(input("Introduzca un número: "))
Numero = int(input("Introduce el número: "))
suma_actual = 0
mult_3_actual = 0
print(f'M={mult_3_actual:2d}: S={suma_actual:2d}')

while suma_actual < Numero:
    mult_3_actual += 3
    suma_actual += mult_3_actual
    print(f'M={mult_3_actual:2d}: S={suma_actual:2d}')
