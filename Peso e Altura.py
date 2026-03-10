import os   
os.system("cls")

Altura_da_pessoa=float(input(" Digite A sua Altura "))

Peso_da_pessoa=float(input(" Digite seu peso "))

imc=Peso_da_pessoa/Altura_da_pessoa**2

print(" Seu imc é ",imc)

if imc < 18.5:
    print(" Abaixo do peso ")

if imc >= 18.5 and imc < 25:
    print(" Peso ideal ")

if imc >= 25 and  imc < 30:
    print(" Sobre peso ")

if imc >= 30 and imc <40:
    print(" Obesidade ")

elif imc > 40:
    print(" Obesidade morbia ")
    
