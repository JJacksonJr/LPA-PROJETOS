import os 

os.system("cls")

Quantidade_de_pessoas_mais_ou_igual_20_anos=0

Soma_idades=0

media_da_idades=0

Quantas_idades_foram_digitadas=0

for i in range (1,6):

    idade=int(input(" Digite Sua idade "))

    Soma_idades+=idade

    media_da_idades= Soma_idades / 5

    if idade > Quantas_idades_foram_digitadas :

        Quantas_idades_foram_digitadas+=1

    if idade >=20 :

        Quantidade_de_pessoas_mais_ou_igual_20_anos+=1

print(" \nA Soma total das idades é de ",Soma_idades)

print("\n A média das  idades é de ",media_da_idades)

print("\n A Quantidade de idades digitadas é de ",Quantas_idades_foram_digitadas)

print("\n A Quantidade de pessoas mais de 20 anos é de ",Quantidade_de_pessoas_mais_ou_igual_20_anos)



    