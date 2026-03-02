import os  
os.system(" cls||clean ")
velocidade_do_carro=float(input(" Qual é a velocidade de carro ?"))

if velocidade_do_carro >80:

    Km_excedidos=velocidade_do_carro-80

    print(" Os Km excedidos. é de ",Km_excedidos, "KM")

    valor_da_multa=Km_excedidos*5

    print(" o valor da multa é de ",valor_da_multa, "R$")

else:

    print(" Não ouve infração, siga seu caminho ")



