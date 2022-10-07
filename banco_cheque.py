 # Banco cheque
print("________________________________________")
print("|             Banco cheque              |")
print("|_______________________________________|")
print("")

#input 
n = 100

n10 = 0
n2 = 0
n1 = 0

while n != 0 :
    n = int(input("Digite la cantidad del cheque: "))
    if n %100 == 0 :
        mil10 = n // 10000
        mil10_1 = n - (mil10 * 10000)
        n10 = n10 + mil10

        mil2 = mil10_1 //2000
        mil2_1 = mil10_1 - (mil2 * 2000)
        n2 = n2 + mil2

        cien1 = mil2_1 //100
        cien1_1 = mil2_1 - (cien1 * 100)
        n1 = n1 + cien1

        print ("El cheque de $",n,"se requiere:")
        print(mil10,"billetes de $10000")
        print (mil2,"billestes de $2000")
        print (cien1,"monedas de $100")
        print("")

    else:
        print("Cantidad no valida, necesita que sea multiplo de $100")

else:
    print("")
    print("RESULTADOS FINALES")
    print(n10,"billetes de $10000")
    print(n2,"billestes de $2000")
    print(n1,"monedas de $100")
    print("")
    
