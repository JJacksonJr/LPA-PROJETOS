import os  
os.system(" cls||clean ")

Ano_nascimento=int(input(" Digite seu Ano de nascimento "))
idade=2026-Ano_nascimento

print(" Sua idade é de ",idade)

if idade <18:
   Anos= idade-18
   print(" Faltam ",Anos, " Para o alistamento ")

else:
   idade>18
   anos=idade-18

   print(" voce já serviu ",anos," No exercito ")