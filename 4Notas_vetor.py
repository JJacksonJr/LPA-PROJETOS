import os

os.system("cls")

vetor_notas=[]

for i in range(0,4):
    notas=int(input(f" Digite sua {i+1} Nota: "))
    vetor_notas.append(notas)

soma= sum(vetor_notas)

media= sum(vetor_notas)/4

for i in range(len(vetor_notas)):
    print(f" Suas Notas {i+1} Digitadas: {vetor_notas[i]}  ")
print(f" A Soma é : {soma}")

if media >= 7:
    print(f" \n media: {media} Aprovado !!")

elif media  >=5 :
    print(f" \n media: {media} Recuperação !!")

elif media < 5:
    print(f" \n media: {media} Reprovado !!")



