
while True: 
    operacio = input("Quina operació vols realitzar? (suma, resta, multiplicació o divisió.). Si vols retirar-te introdueix sortir: \n")
    if operacio == "sortir":
        break
    else:
        num1 = float(input("Introdueix el primer nombre de l'operació: \n"))
        num2 = float(input("Introdueix el segon nombre de l'operació: \n"))
        
        if operacio == "suma":
            print (num1+num2)
        elif operacio == "resta":
            print (num1-num2)
        elif operacio == "multipliació":
            print (num1*num2)
        elif operacio == "divisió":
            if num2 == 0:
                print("Error: no es pot dividir un nombre entre 0.")
            else:
                print (num1/num2)
        else: 
            print("Operació no vàlida.")

