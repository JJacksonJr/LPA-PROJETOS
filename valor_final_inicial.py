import os  

os.system("cls")

Digite_inicio=int(input(" Digite o valor inicial "))

Digite_final=int(input(" Digite o valor final "))

if Digite_inicio < Digite_final :

    for i in range(Digite_inicio,Digite_final+1) :#crescente

        print(i)

else:
    for i in range(Digite_inicio,Digite_final-1,-1) :#decrescente

        print(i)