import os  
os.system("cls||clean")

Nome=str(input(" Digite seu Nome "))
Nota1=int(input(" Diga sua primeira Nota "))
Nota2=int(input(" Digite sua segunda Nota "))

print(" olá " ,Nome)

print(" Sua primeira Nota é ",Nota1)

print(" Sua segunda Nota é de ",Nota2)

média=(Nota1+Nota2)/2

print(" Sua média é de ",média)

if média >=7:
    print(" Otimo Aproveitamento ")

else:

    print(" Não teve um bom Aproveitamento ")