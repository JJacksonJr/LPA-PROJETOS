import os 

os.system("cls")

jogador_1 = input("Escolha pedra | papel | tesoura jogador 1 = ").lower()

jogador_2 = input("Escolha pedra | papel | tesoura jogador 2 = ").lower()


if jogador_1 == "pedra" and jogador_2 == "tesoura":

    print(" Jogador 1 venceu ")

if jogador_1 == "papel" and jogador_2 == "pedra":

    print(" jogador 1 venceu ")

if jogador_1 == "tesoura" and jogador_2 == "papel":
    
    print(" Jogador 1 venceu ")

if jogador_2 == "pedra" and jogador_1 == "tesoura":

    print(" Jogador 2 venceu ")

if jogador_2 == "papel" and jogador_1 == "pedra":

    print(" jogador 2 venceu ")

if jogador_2 == "tesoura" and jogador_1 == "papel":
    
    print(" Jogador 2 venceu ")

if jogador_1 == "pedra" and jogador_2 == "pedra":

    print("EMPATE")

if jogador_1 == "papel" and jogador_2 == "papel":

    print("EMPATE")

if jogador_1 == "tesoura" and jogador_2 == "tesoura":

    print("EMPATE")