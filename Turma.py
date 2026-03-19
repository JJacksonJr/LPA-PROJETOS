import os 

os.system("cls")

Soma_total_Das_notas=0

Media_ari=0

Alunos_existentes=int(input("Digite Quantos alunos existem "))

for i in range(Alunos_existentes):
    
    Notas=float(input("Digite A sua nota"))

    Soma_total_Das_notas+=Notas


Media_ari= Soma_total_Das_notas / Alunos_existentes

print(f" A soma total é de {Soma_total_Das_notas}")

print(f"A média total é de {Media_ari}")