import os 

os.system("cls")

Vetor_notas=[]


for i in range(0,3):
    notas=int(input(f" Digite {i+1} Nota "))

    Vetor_notas.append(notas)

for i in range(len(Vetor_notas)):
    print(f" Sua {i+1} Notas:  {Vetor_notas[i]}")

