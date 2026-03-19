import os 

os.system("cls")

Quantos_são_Negativo=0


for i in range  (1,11):
    
    ler=int(input("Digite um valor "))

    if ler <0:
        Quantos_são_Negativo+=1


print(f"Quantidade são negativos {Quantos_são_Negativo}")
