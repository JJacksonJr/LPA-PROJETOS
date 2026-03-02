import  os  
os.system("cls||clean")

Distancia_KM=float(input(" Qual é a distancia que vc quer pecorrer"))

if Distancia_KM < 200:
    preço_da_passagem=Distancia_KM*0.50

    print(" O valor da passagem é de ",preço_da_passagem,"$$")

else:
    Distancia_KM>=200
    preço_da_passagem=Distancia_KM*0.45

    print(" O valor da passagem em sua viagem longa é d e",preço_da_passagem"$$")
