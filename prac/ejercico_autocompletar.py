#Crear una lista con los cuadrados de los n primeros números naturales
def cuadrados(n):
    return [i**2 for i in range(1, n+1)]

print(cuadrados(10))

#Crear una función que calcule la suma de los cuadrados de los n primeros números naturales
def suma_cuadrados(n):
    return sum(cuadrados(n))

print(suma_cuadrados(10))
