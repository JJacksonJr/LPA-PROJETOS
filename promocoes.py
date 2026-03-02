import os   
os.system(" cls||clean ")
Nome=str(input(" Digite seu Nome "))
Sexo=str(input(" Digite Seu Sexo "))

Valor_da_compra=float(input(" Digite o valor da sua compra "))
Desconto_H=0.05
Desconto_M=0.13

if Sexo=="Homem":
  desconto_final=Valor_da_compra*Desconto_H
  valor_final=Valor_da_compra-desconto_final
  print(" Homem,o valor da sua compra é de ",valor_final)

else:
  Sexo=="Mulher"
  desconto_final_M=Valor_da_compra*Desconto_M
  valor_final_M=Valor_da_compra-desconto_final_M

  print(" Mulher o valor da sua compra é de ",valor_final_M)