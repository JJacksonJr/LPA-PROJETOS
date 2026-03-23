import os 

os.system("cls")

Contador_50=0
Contador_20=0
Contador_10=0
Contador_1=0

valor_a_ser_sacado=int(input("Digite o valor a ser sacado"))

while valor_a_ser_sacado > 0:

    print("====Banco=======")
    

    if valor_a_ser_sacado >=50:
        valor_a_ser_sacado -= 50
        Contador_50+=1

    elif valor_a_ser_sacado >= 20:
        valor_a_ser_sacado-=20
        Contador_20+=1

    elif valor_a_ser_sacado >=10:
        valor_a_ser_sacado-= 10
        Contador_10+=1

    elif valor_a_ser_sacado >=1 :
        valor_a_ser_sacado -=1 
        Contador_1+=1


print(f"Notas de 50: {Contador_50}")
print(f" Notas de 20: {Contador_20}")
print(f" Notas de 10: {Contador_10}")
print(f" Notas de 1:{Contador_1}")

        
