import os   
os.system("cls")
valor_da_casa=float(input(" Digite o valor da casa?:"))

salário_comprador=float(input(" Digite seu salário "))

Quantos_anos_vai_pagar=int(input(" Digite Quantos anos  vai pagar "))

Meses=Quantos_anos_vai_pagar*12

prestaçao=valor_da_casa/Meses

Limite=salário_comprador*0.30#30%=30/100=0.30

if prestaçao <=Limite:
    print(" Emprestimo Aprovado ")

else:
    print(" Emprestimo Negado")


print(" Meses:",Meses)

print(" prestações",prestaçao)

print(" Limite ",Limite)