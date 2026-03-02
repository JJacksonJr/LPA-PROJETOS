import os  
os.system(" cls||clean ")
Km=float(input(" DIgite quantos Km andou o carro "))
dias=int(input("Quantos dias foi alugado ? ")) 
#0.20 por km andado
#aluguel 90 por dia
Km_por_rodado=Km*0.20
total_dias=dias*90

print(" valor por Km rodado ",Km_por_rodado)
print(" preço  alugado por 90, nos dias de que alugou  ",total_dias)

preço_total=Km_por_rodado+total_dias
print(" preço total a pagar é de  ",preço_total)

