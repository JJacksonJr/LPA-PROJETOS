import os 

os.system("cls")

vetor_numero=[]

qtd_negativo=0

soma=0
for i in range(0,5):
    numero=int(input(f" digite {i+1} Numero : "))

    vetor_numero.append(numero)

    if numero < 0 :
        qtd_negativo+=1

    





for i in range(len(vetor_numero)):

    if vetor_numero[i] > 0 :
        soma+=vetor_numero[i]

print(f" A quantidade de Numeros negativos é de: {qtd_negativo} e A Soma dos posistivos  {soma} ")