import os 

os.system("cls")

Soma_dos_salarios=0
contador_de_pessoas=0
Maior_idade=0
Menor_idade=0
contador_De_mulheres_de_5000_reais=0
media_do_grupo_salario=0


while True:
    Menu=int(input(" Qual Menu vc quer ? // 1 Adcionar pessoa // 2 mostra_pessoas // 3 Sair"))
    os.system("cls")
    match Menu :

        case 1 :
            print("Adicionando pessoa")

            idade=int(input(" Digite sua idade"))

            Sexo=str(input(" Digite seu sexo M ou F")).strip()

            Salario=float(input(" Digite seu sálario"))

            Soma_dos_salarios+=Salario

            contador_de_pessoas+=1

            if contador_de_pessoas== 1:

                Maior_idade=idade
                Menor_idade=idade

            if idade > Maior_idade:
                Maior_idade= idade

            if idade < Menor_idade:
                Menor_idade=idade

            if Sexo == "F" and Salario >= 5000:
                contador_De_mulheres_de_5000_reais+=1
                os.system("cls")

                


        case 2 :
            print("Mostrando REsultado")

            media_do_grupo_salario= Soma_dos_salarios / contador_de_pessoas

            print(f" A media do salario do grupo é de : {media_do_grupo_salario}")
            print(f" A maior idade é : {Maior_idade}")
            print(f" A menor idade é : {Menor_idade}")
            print(f" A Quantidade de mulheres de 5000 reais acima é : {contador_De_mulheres_de_5000_reais}")
            print(f" A quantidade de pessoas cadastradas: {contador_de_pessoas}")
            

        case 3:
            break

