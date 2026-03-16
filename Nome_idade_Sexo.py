import os  

os.system("cls")

Soma_idades=0

Media_da_idade_grupo=0

Maior_idade_do_Homem=0

Nome_do_mais_velho=""

Mulheres_menos_20=0

for i in range (1,5):
    Nome=str(input(" \nDigite seu Nome:  ")).strip()

    idade=int(input(" \nDigite Sua idade:  "))

    Sexo=str(input(" \nDigite Seu Sexo H ou F:   ")).strip()

    Soma_idades+=idade

    Media_da_idade_grupo= Soma_idades / 4 

    if i ==1 and Sexo == "H":

        Maior_idade_do_Homem=idade
        Nome=Nome_do_mais_velho

    if  Sexo == "H" and idade > Maior_idade_do_Homem :

        Maior_idade_do_Homem=idade

        Nome_do_mais_velho= Nome

    if Sexo == "F" and idade < 20 :

        Mulheres_menos_20+=1







print(" A média do grupo é de ",Media_da_idade_grupo," Anos ")
print(" O Nome do mais velho é de ",Nome_do_mais_velho, " e  A maior idade é de ",Maior_idade_do_Homem)
print(" Ao Todo tem um total de ",Mulheres_menos_20," Menos de 20 anos mulheres ")




