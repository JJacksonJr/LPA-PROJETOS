import os 

os.system(" cls ")


Peso_Maior=0
peso_menor=0

for i in range (1,6):

    Peso_do_cliente=float(input(" Digite o seu peso "))

    if Peso_do_cliente > Peso_Maior :
        
        Peso_Maior = Peso_do_cliente

        peso_menor=Peso_do_cliente

    if Peso_do_cliente < peso_menor :

        peso_menor= Peso_do_cliente

print(" O Maior peso é de ",Peso_Maior," O Peso Mneor é de ",peso_menor)
