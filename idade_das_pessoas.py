import os 

os.system("cls")


media_do_grupo_idade=0

Soma_das_idades=0

Maior=0


Quantidades_Maior_de_18=0

Quantidades_Menor_de_5=0

for i in range(1,11):

    idade=int(input("\nDigite a sua idade"))

    Soma_das_idades+=idade

    if i==1:

        Maior=idade

    else:

        if idade > Maior:

            Maior=idade

    if idade >18:

        Quantidades_Maior_de_18+=1

    if idade < 5:

        Quantidades_Menor_de_5+=1


media_do_grupo_idade= Soma_das_idades/10

print(f"A Soma das idades do grupo é de {Soma_das_idades}")
print(f"A média do grupo é de {media_do_grupo_idade}")
print(f"A Quantidade maior de 18 anos é de {Quantidades_Maior_de_18}")
print(f"A Quantidade menor que 5 anos é de {Quantidades_Menor_de_5}")
print(f"A idade maior lida é de {Maior}")