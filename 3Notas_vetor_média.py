import os 

os.system("cls")


vetor_notas=[]


for i in range(0,3):
    nota=int(input(f" Digite sua {i+1} Nota: "))
    vetor_notas.append(nota)


media= sum(vetor_notas) / 3

print(f" Sua média é de : {media} ")