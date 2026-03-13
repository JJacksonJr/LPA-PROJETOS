import os 

os.system("cls")


Soma=0

for i in range (1,7) :

    Numero=int(input(" Digite um Numero "))

    if Numero % 2 == 0 :

        Soma+=Numero

    else:

        print(" Desconsidere ")

print("   O VAlor total da soma é de ",Soma)



