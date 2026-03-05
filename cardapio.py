import os   
os.system("cls")



print("""
     
     //================MENU================= //
    //  codigo        prato        preço     //
    //                                       //
    //   1          Picanha       25,00 $    //
    //                                       //
    //   2          Lasanha       20,00 $    //
    //                                       //
    //  3          Strogonoff    18,00 $    //
    //                                      // 
    // 4        Bife Acebolado  15,00 $     //
    //                                      //
    // 5         Pão com ovo    5,00 $     //
    //                                     //
      ===============MENU==================//
      
      """)

prato_usuario=int(input(" Digite o codigo do Menivis "))

match prato_usuario:

    case 1:
        print("Picanha= preço 25,00$")
        
    case 2:
        print(" Lasanha= 20,00 $")
        
    case 3:
        print(" Strogonoff= 18,00 $")
        
    case 4:
        print(" Bife Acebolado= 15,00 $ ")
        
    case 5:
        print(" Pão com ovo= 5,00 $")
        
    case _:
        print(" Prato invalido ")
        
print("..................Fim do programa.....................")