import os  
os.system("cls||clean")
largura=int(input(" Digite a  largura " ))
comprimento=int(input(" Digite o comprimento"))

Area=largura*comprimento

print("Area:",Area," m² ")

if Area<100:
    print(" Terreno Popular ")

if Area>=100 and Area<500:
    print("Terreno Master ")

elif Area >=500:
    print(" Terreno Vip")