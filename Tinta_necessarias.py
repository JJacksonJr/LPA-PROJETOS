import os   
os.system(" cls || clean ")

largura=int(input(" Digite a Largura da parede "))
altura=int(input(" Digite a Altura da parede "))

área=largura*altura

print(" A área a ser pintada é de ",área)

tintas_necessarias=área/2

print("A quantidade de tintas necessarias pra ser pintada é de ",tintas_necessarias)