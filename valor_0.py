import os 

os.system("cls")

vetor_5=[]


for i in range(0,5):
    numero=int(input(f" Digite {i+1} Numero  "))

    vetor_5.append(numero)

    if numero < 0:
        vetor_5[i]=0

for i in range(len(vetor_5)):
    print(f" valores: {vetor_5[i]}")