import os  

os.system("cls")
Menores=0
Maioridade=0
for i in range (1,8,1):

    Ano_nascimento=int(input(" Digite o ano do seu Nascimento"))

    idade=2026-Ano_nascimento

    if idade < 18 :

        Menores+=1

    if idade >18 :

        Maioridade+=1


print(" A QUantidade de maiores é de ",Maioridade)

print(" A QUantidade é de menores é de ",Menores)



   