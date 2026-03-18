import os 

os.system("cls")

Quantos_Homens_cadastrados=0

Quantas_Mulheres_cadastradas=0

Soma_total_idades=0

media_do_grupo=0

media_idades_homens=0

Quantas_mulheres_tem_mais_20_anos=0

idade_total_Homens=0



for i in range (1,6):

    Sexo=str(input(" \nDigite seu sexo M ou F: ")).strip()

    idade=int(input("\nDigite sua idade: "))

    if Sexo =="M" :

        idade_total_Homens+=idade

        Quantos_Homens_cadastrados+=1

    else:
        if Sexo =="F" and idade > 20:

            Quantas_mulheres_tem_mais_20_anos+=1

            Quantas_Mulheres_cadastradas+=1


    Soma_total_idades+=idade

media_do_grupo= Soma_total_idades /5

media_idades_homens= idade_total_Homens / Quantos_Homens_cadastrados

print(f" Soma total das idades dos Homens é de {idade_total_Homens}")

print(f"A Soma total das idades é de {Soma_total_idades}")

print(f"Foram cadastrados {Quantos_Homens_cadastrados} Homens")

print(f"Foram cadastrados {Quantas_Mulheres_cadastradas} Mulheres")

print(f" A média do grupo é de  {media_do_grupo} :")

print(f"A média do grupo de Homens é de  {media_idades_homens} :")

print(f" Tem {Quantas_mulheres_tem_mais_20_anos} mulheres acima de 20 anos")
