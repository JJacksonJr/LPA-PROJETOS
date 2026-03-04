import os
os.system("cls||clean")

Nota1=float(input(" Digite sua primeira Nota"))
Nota2=float(input(" Digite sua segunda Nota"))

media=(Nota1+Nota2)/2

print(" Sua média é de ",media)


if media<4.9:
    print(" Reprovado")

if media >=5.0 and media <6.9:
    print("  voce está em Recuperação")

elif media>=7.0:
    print(" Aprovado")