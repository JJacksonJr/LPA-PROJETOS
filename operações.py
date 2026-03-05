import os  
os.system("cls")

Numero1=int(input(" Digite um Numero "))
Numero2=int(input(" Digite um Numero "))
caractere=str(input(" escolha sua operação + - * /")).strip()#Remove o espaço,só em texto


match caractere:
    case "+":
        valor1=Numero1+Numero2
        print(" O valor da soma é de ",valor1)
    
    case "-":
        valor2=Numero1-Numero2
        print(" O valor da subtração é de ",valor2)
    
    case "*":
        valor3=Numero1*Numero2
        print(" O valor da multiplicação é de",valor3)
        
    case "/":
        valor4=Numero1/Numero2
        print(" O valor da divisão é de ",valor4)
        
    case _:
        print(" Digite + _ * / para poder realizar a operação ")
        
        
print(" ..............Fim do programa.................")