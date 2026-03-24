import os 

os.system("cls")

Quantidade_de_pares=0
Quantidade_de_impares=0

Soma_total_dos_pare=0
media_total_dos_pares=0

Soma_total_de_tudo=0
media_de_tudo=0

Contador_de_tudo=0

while True :
    valores=int(input(" Digite um valor "))

    if valores== 0:
        print(" Parando")
        break

    else:
        Soma_total_de_tudo+=valores
        Contador_de_tudo+=1

    if valores % 2 == 0:
        Soma_total_dos_pare+=valores
        Quantidade_de_pares+=1

    else:
        Quantidade_de_impares+=1


media_de_tudo= Soma_total_de_tudo / Contador_de_tudo

media_total_dos_pares= Soma_total_dos_pare / Quantidade_de_pares


print(f" A média de tudo é de: {media_de_tudo}")
print(f" A méida total de pares é de: {media_total_dos_pares}")
print(f" A Quantidade de pares é de: {Quantidade_de_pares}")
print(f" A Quantidade de impares: {Quantidade_de_impares}")


