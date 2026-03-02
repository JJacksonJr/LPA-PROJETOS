import os   
os.system("  cls||clean ")
Ano=int(input(" Digite um Ano "))
#Ele tem que ser divisivel por 4, Não pode ser divisivel por 100, e tem que ser divisivel por 400
if (Ano %4==0 and Ano % 100 !=0) or (Ano %400==0):

    print(" È bissexto ")

else :

    print(" Não é bissexto ")