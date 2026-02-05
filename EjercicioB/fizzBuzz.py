# FizzBuzz: Recorrer números del 1 al 50. Si el número es mĺtiple de 3, imprimir "Fizz"; de 5, imprimir "Buzz"; de ambos, "FizzBuzz"; si no, e número.
for i in range(1,51):
    if (i % 3) == 0 and (i % 5 ) == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)