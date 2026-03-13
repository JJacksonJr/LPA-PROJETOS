import os  
os.system("cls")

soma=0
for i in range (1,501,2) :# o dois tira os Numeros pares   

    if i % 3== 0:

        soma+=i
print(" A Soma Total impares  é de ",soma)