import os  
os.system("cls||clean")

preço=float(input(" Digite o preço do produto"))
#5%=5 por cem 5/100=0.05

desconto=preço*0.05
print(" seu desconto é de ",desconto)

preço_promocional=preço-desconto

print(" seu valor final é de ",preço_promocional)

