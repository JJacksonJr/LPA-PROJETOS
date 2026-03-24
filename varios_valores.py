import os 

os.system("cls")

Soma_total=0
media_ari=0
contador=0

while True:
    varios_valores=int(input("Digite o valor "))

    if varios_valores < 0:
        break

    else:
        Soma_total+=varios_valores
        contador+=1


media_ari=Soma_total/contador


print(f" A média total é de: {media_ari}")


