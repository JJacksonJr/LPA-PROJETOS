import os  
os.system("cls")

Sexo=str(input(" Digite seu Gênero Homem ou Mulher")).strip()

salario_atual=int(input(" Digite seu salário Atual "))

Quantos_anos_voce_trabalha_na_empresa=int(input(" Digite quantos anos voce trabalha na Empresa"))

if Sexo =="Mulher":

    if Quantos_anos_voce_trabalha_na_empresa <=15 :

        Aumento= salario_atual * (5/100)

        salario_final = salario_atual + Aumento

        print(" SEu Aumento é de ",Aumento)

        print(" Seu Salaário Final é de ",salario_final)

    if Quantos_anos_voce_trabalha_na_empresa > 15 and Quantos_anos_voce_trabalha_na_empresa <=20 :

        Aumento= salario_atual * (12/100)

        salario_final= salario_atual + Aumento

        print(" Seu Aumento é de ",Aumento)

        print(" Seu salário Final é de ",salario_final)

    if Quantos_anos_voce_trabalha_na_empresa > 20 :

        Aumento= salario_atual * (23/100)

        salario_final= salario_atual + Aumento

        print(" Mulher:Seu Aumento é de ",Aumento)

        print(" Mulher: Seu Salário Final é de ",salario_final)

elif Sexo == "Homem" :

    if Quantos_anos_voce_trabalha_na_empresa <= 20 :

        Aumento= salario_atual * (3/100)

        salario_final= salario_atual + Aumento

        print(" Homem: Seu Aumento é de ", Aumento)

        print(" Homem:  Seu Salário Final é de ",salario_final)

    if Quantos_anos_voce_trabalha_na_empresa > 20 and Quantos_anos_voce_trabalha_na_empresa <=30 :

        Aumento= salario_atual * (13/100)

        salario_final= salario_atual + Aumento

        print("Homem: Seu Aumento é de ",Aumento)

        print(" Homem: Seu Salario final é de " , salario_final)

    if Quantos_anos_voce_trabalha_na_empresa > 30 :

        Aumento= salario_atual * (25/100)

        salario_final= salario_atual + Aumento

        print(" Homem: Seu Aumento é de " , Aumento)

        print(" Homem: Seu Salario Final é de ",salario_final)