import os 

os.system("cls")



while True :
        Numero=int(input("Digite um Numero para a tabuada"))

        if Numero < 0 or Numero > 10 :
                break

        for i in range (1,11):
              
               Resultado= Numero * i
               
               print(f"{Numero} * {i} = {Resultado}")
    