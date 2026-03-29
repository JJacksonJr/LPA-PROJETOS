import os 

os.system("cls")

prato_escolhido=[]

preco_do_prato=[]

valor_total=0



while True:

    print("""
    === MENU ===
    1   Picanha          R$ 25,00
    2   Lasanha          R$ 20,00
    3   Strogonoff       R$ 18,00
    4   Bife acebolado   R$ 15,00
    5   Pão com ovo      R$ 15,00
        """)
    
    opçao=int(input(" escolha de 1 a 6 "))

    match opçao:

        case 1:
            prato_escolhido.append("Picanha")

            preco_do_prato.append(25.0)

            valor_total+=25

            continuar=str(input("deseja continuar ? S ou N ")).strip().lower()

            if continuar =="n":
                break

        case 2:
            prato_escolhido.append("Lasanha")

            preco_do_prato.append(20.0)

            valor_total+=20

            continuar=str(input("deseja continuar ? S ou N ")).strip().lower()

            if continuar =="n":
                break

        case 3:
            prato_escolhido.append("Strogonoff")

            preco_do_prato.append(18.0)

            valor_total+=15

            continuar=str(input("deseja continuar ? S ou N ")).strip().lower()

            if continuar =="n":
                break

        case 4:
            prato_escolhido.append("Bife acebolado")

            preco_do_prato.append(15.0)

            valor_total+=15

            continuar=str(input("deseja continuar ? S ou N ")).strip().lower()

            if continuar =="n":
                break

        case 5:
            prato_escolhido.append("Pão")

            preco_do_prato.append(5.0)

            valor_total+=5

            continuar=str(input("deseja continuar ? S ou N ")).strip().lower()

            if continuar =="n":
                break

        case _:
            print(" Digite Novamente")

for i in range(len(prato_escolhido)):
    print(f" {prato_escolhido} - {preco_do_prato}")




print(f" O valor total é de: {valor_total}")

pagar=int(input(" digite o valor pra pagar "))

troco=valor_total-pagar

print(f" o troco foi de : {troco}")
    