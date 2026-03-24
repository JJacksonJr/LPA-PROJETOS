import os 

os.system("cls")


Login_verdadeiro=2008

Senha_verdadeira="Mecua"

for i in range(1,4):
    while True:
        login=int(input("Digite seu login "))

        Senha=str(input(" Digite sua senha ")).strip()

        if login == 2008 and Senha == "Meuca":
            print(" Seja bem vindo Meuca")
            break

        else:
            print(" Digite novamente ")
            break
        