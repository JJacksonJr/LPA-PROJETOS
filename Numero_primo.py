import os  

os.system("cls")

Numero=int(input(" Digite um Numero "))

primo=True

for i in range (2,Numero,1):

    if Numero % 1 == 0 :

        primo= False




if primo :

    print(" È primo ")

else :

    print(" Não é primo ")