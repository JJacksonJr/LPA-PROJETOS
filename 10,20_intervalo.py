import os 

os.system("cls")

Contar_quantos_tem_dentro=0

Contar_quantos_tem_fora=0

for i in range (1,11):

    ler=int(input("Digite um valor"))


    if ler >=10 and ler <= 20:
       Contar_quantos_tem_dentro+=1

    else:
        Contar_quantos_tem_fora+=1
       


print(f"A quantidade dentro é de {Contar_quantos_tem_dentro}")
print(f"A quantidade Fora é de {Contar_quantos_tem_fora}")