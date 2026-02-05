#Determinar si un número es primero
print("Determinar si un número es primero : Versión original de la IA")
def num_es_primero(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(num_es_primero(1))
print(num_es_primero(2))
print(num_es_primero(3))
print(num_es_primero(4))
print(num_es_primero(5))
print(num_es_primero(6))

#Determinar si un número es primero : Versión optimitzada de la IA
print("Determinar si un número es primero : Versión optimitzada de la IA")
def num_es_primero(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # Comprobamos solo impares desde 3 hasta sqrt(num)
    limite = int(num ** 0.5) + 1                    # Si aquí ponemos -1 la IA efectivamente nos detecta el error.
    for i in range(3, limite, 2):
        if num % i == 0:
            return False
    return True

# Pruebas básicas
print(num_es_primero(1))   # Esperado: False
print(num_es_primero(2))   # Esperado: True
print(num_es_primero(3))   # Esperado: True
print(num_es_primero(4))   # Esperado: False
print(num_es_primero(17))  # Esperado: True
print(num_es_primero(18))  # Esperado: False

#Prueba de la función num_es_primero mediante un bucle for.
print("Prueba de la función num_es_primero mediante un bucle for.")
for n in range(1, 31):
    print(n, "->", num_es_primero(n))

#Prueba de la función num_es_primero mediante assert.
print("Prueba de la función num_es_primero mediante assert.")
def probar_num_es_primero():
    assert num_es_primero(1) is False
    assert num_es_primero(2) is True
    assert num_es_primero(3) is True
    assert num_es_primero(4) is False
    assert num_es_primero(17) is True
    assert num_es_primero(18) is False
    print("Todas las pruebas han pasado correctamente")

probar_num_es_primero()