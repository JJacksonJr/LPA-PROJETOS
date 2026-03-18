import os 

os.system("cls")

Maior=0
Menor=0

for i in range(1,9):

    produtos_preço=int(input("Digite o valor do protduto"))

    if i==1:
        Maior=produtos_preço
        Menor=produtos_preço

    else:
        if produtos_preço > Maior:
            Maior=produtos_preço

        if produtos_preço < Menor:
            Menor=produtos_preço

print(f"O Maior preço é de {Maior}")
print(f"O Menor preço é de {Menor}")