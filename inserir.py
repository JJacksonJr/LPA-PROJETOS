import os 

os.system("cls")

Soma_total_das_notas=0

contador=0
media=0
while True:
    Nota=int(input("Deseja inserir uma nota "))

    Soma_total_das_notas+=Nota

    contador+=1

    Resposta=str(input(" deseja adicionar mais uma nota S ou N "))

    if Resposta == "N":
        break

media=Soma_total_das_notas / contador
print(f" A soma total é de {Soma_total_das_notas}")
print(f" A média Total é de : {media}")

