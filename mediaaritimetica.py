import os 

os.system("cls")

media_ari=0
Soma_total=0

for i in range(1,11):

    ler=int(input(" Digite o valor aí "))

    Soma_total+=ler


media_ari= Soma_total / 10

print(f"O valor total é de {Soma_total}")

print(f" A média é de {media_ari}")