import os 

os.system("cls")

Quantidade_impar=0
Quantidade_pares=0

for i in range(1,7):

    Numero=int(input(" Digite um Numero "))

    if Numero % 2==0:
        Quantidade_pares+=1

    else:
        Quantidade_impar+=1

print(f" A Quantidade de pares é de {Quantidade_pares} e de impares é de {Quantidade_impar}")