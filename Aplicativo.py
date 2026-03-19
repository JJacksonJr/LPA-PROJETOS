import os 

os.system("cls")

Quantas_pessoas_mais_de_90=0

Soma_dos_pesos=0

media_da_altura_grupo=0

Soma_total_das_alturas=0

Quantas_pessoas_pesam_menos_de_50_Kg_e_tem_menos_De_1_60_Altura=0

Quantas_pessoas_tem_mais_de_90_ALtura_e_pesam_mais_De_100kg=0





for i in range (1,8):

    
    Altura=float(input("\nDigite o valor da Altura"))


    print("=======================================")

    Peso=float(input("\nDigite o Seu peso "))


    Soma_total_das_alturas+=Altura


    if Peso > 90 :
        Quantas_pessoas_mais_de_90+=1

    if Peso < 50 and Altura < 1.60:
        Quantas_pessoas_pesam_menos_de_50_Kg_e_tem_menos_De_1_60_Altura+=1

    if Altura > 1.90 and Peso > 100:
        Quantas_pessoas_tem_mais_de_90_ALtura_e_pesam_mais_De_100kg+=1


media_da_altura_grupo= Soma_total_das_alturas / 7

print(f"A média da altura do grupo é de : {media_da_altura_grupo} ")
print(f" A Quantidade de pessoa que pesam mais de 90kg é de : {Quantas_pessoas_mais_de_90}")
print(f"A Quantidade de pessoa que pesam menos de 50kg e tem menos de 1.60m : {Quantas_pessoas_pesam_menos_de_50_Kg_e_tem_menos_De_1_60_Altura}")
print(f"A Quantidade de pessoas que medem mais de 1.90 m e pesa mais de 100 kg : {Quantas_pessoas_tem_mais_de_90_ALtura_e_pesam_mais_De_100kg}")


