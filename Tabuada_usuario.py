import os 

os.system("cls")

Tabuada_usuario=int(input("Digite um valor da sua tabuada"))

for i in range(1,11):

    Resutlado = Tabuada_usuario * i

    print(f"{Tabuada_usuario} * {i} = {Resutlado}")