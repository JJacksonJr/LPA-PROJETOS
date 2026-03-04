import os  
os.system("cls||clean")
Nome_funcionario=str(input(" Digite seu nome "))
salario=int(input(" Digite seu sálario"))
Anos_empresas=int(input(" Quantos anos na empresa"))

if Anos_empresas < 3:
    Aumento=salario*0.03 # 3%=3/100
    salario_final=salario+Aumento

    print(" Seu salario é de ",salario_final)

if Anos_empresas>=3 and Anos_empresas<10:
    Aumento=salario*0.125 #12,5%=12,5/100
    salario_final=salario+Aumento

    print(" Seu salário é de ",salario_final)

elif Anos_empresas>=10:
    Aumento=salario*0.2 #20%=20/100
    salario_final=salario+Aumento

    print(" Seu salário é de ",salario_final)