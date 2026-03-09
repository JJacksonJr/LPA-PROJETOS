import os  
os.system(" cls ")

Tipo_de_carro_Alugado=str(input(" Escolha o tipo de carro alugado: carros populares || carros luxos ")).strip().lower()

Quantos_dias_de_aluguel=int(input(" Digite Quantos dias vc Alugou"))

Quantos_KM_Pecorridos=int(input(" Digite a Quantidas de Km pecorridos "))


if Tipo_de_carro_Alugado == "carros populares":

    Total_Pago_dias = Quantos_dias_de_aluguel * 90

    if Quantos_KM_Pecorridos <= 100:
        
        valor_Total_KM_pra_pagar = Quantos_KM_Pecorridos * 0.20

    if Quantos_KM_Pecorridos > 100:

     valor_Total_KM_pra_pagar = Quantos_KM_Pecorridos * 0.10

    print("KMS pecorridos é de ",Quantos_KM_Pecorridos)

    print(" Populares: O valor total pago por dias é de ",Total_Pago_dias," $$ e o valor Total de Km pecorridos pra pagar  é de ",valor_Total_KM_pra_pagar)

elif Tipo_de_carro_Alugado == "carros luxos":

    Total_Pago_dias_2 = Quantos_dias_de_aluguel * 150

    if Quantos_KM_Pecorridos <= 200 :

        valor_Total_KM_pra_pagar_2 = Quantos_KM_Pecorridos * 0.30

    if Quantos_KM_Pecorridos > 200:

         valor_Total_KM_pra_pagar_2 = Quantos_KM_Pecorridos * 0.25

    print(" KMS pecorridos é de ",Quantos_KM_Pecorridos)

    print(" Luxo: O valor Total pago por dias é de",Total_Pago_dias_2 ," $$ , e o valor total de km pecorridos pra pagar é de" ,valor_Total_KM_pra_pagar_2," $$")

