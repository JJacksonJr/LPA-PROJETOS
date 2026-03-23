import os 

os.system("cls")

Total_gasto_na_compra=0

Quantos_produtos_custam_mais_De_1000=0

Nome_do_produto_mais_barato=""

Menor_preço=0


while True :
    
    Nome_do_produto=str(input(" Digite o Nome do Produto ")).strip()


    preço_do_produto=float(input(" Digite o valor do produto"))

    Total_gasto_na_compra+=preço_do_produto

    if Nome_do_produto_mais_barato == "":
        Menor_preço=preço_do_produto
        Nome_do_produto_mais_barato=Nome_do_produto
    else:
        if preço_do_produto < Menor_preço :
            Menor_preço=preço_do_produto
            Nome_do_produto_mais_barato=Nome_do_produto

    print("===============================================")


    if preço_do_produto > 1000 :

        Quantos_produtos_custam_mais_De_1000+=1

    Resposta=str(input("Deseja continuar ou N ?  S= para continuar e P = para Parar")).strip()

    if Resposta == "S":
        continue

    if Resposta == "P":
        break


print(f" \n O Total gasto é de : {Total_gasto_na_compra}")
print(f" A Quantidade de produtos que custam mais de 1000$ é de: {Quantos_produtos_custam_mais_De_1000}")
print(f" O Nome do Produto mais barato é de : {Nome_do_produto_mais_barato}")


    