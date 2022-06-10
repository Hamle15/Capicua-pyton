#Hamlet Pirazan

class Final:



    def palindromo(word):
        
            if str(word) == "".join(reversed(word)) :
                print("Palindroma")
            else:
                print("No es Palindroma")

    def capicua(word):
        
            if str(word) == "".join(reversed(word)) :
                print("Capicua")
            else:
                print("No es Capicua")


    salir = 1

    while salir !=0:
        print("Digite 1 si desea comprobar palidromo o 2 si es capicua")
        print(" ")
        opc = int(input("Digite su opcion: "))
        print(" ")

        if opc == 0:
            break
        elif opc == 1:
            a=input("Digite su palabra palidromo: ")
            
            print(palindromo(a))
        elif opc == 2:
            b = (input("Digite su numero: "))

            print(capicua(b))
        else:
            print("Eliga una opcion correcta")
        print
        salir =int(input("Si desea salir digite 0, si  no cualquier otro numero: "))
        print("")