import os  
os.system(" cls")

dia=str(input(" Digite dia da semana")).strip()

match dia:
    case "Segunda":
        print(" Hoje é segunda ")
    
    case "Terça feira":
        print(" Hoje é terça feira ")
        
    case "Quarta feira":
        print(" Hoje é Quarta feira ")
        
    case "Quinta feira":
        print(" Hoje é Quinta feira ")
        
    case "Sexta feira":
        print(" hoje é Sexta feira ")
        
    case "Sábado":
        print(" hoje é Sábado ")
        
    case "Domingo":
        print(" Hoje é Domingo ")
        
    case _:
        print(" Dia invalido")
        
print(dia)
    
print(" ..................Fim..................")