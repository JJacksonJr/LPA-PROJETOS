import os  
os.system(" cls||clean ")
cigarros_fumados_por_dia=int(input(" Quantos cigarros voce fumou ?"))
quantos_anos_fumou=int(input("Quantos anos voce fumou"))

total_de_dias_que_fumou=quantos_anos_fumou*365

total_de_cigarros_que_fumou=total_de_dias_que_fumou*cigarros_fumados_por_dia

total_de_minutos_perdidos_De_vida=total_de_cigarros_que_fumou*10

total_de_dias_perdidos_de_vida=total_de_minutos_perdidos_De_vida/1440

print(" Total de vida perdida por fumar é de ",total_de_dias_perdidos_de_vida)

