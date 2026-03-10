import os   
os.system("cls")

Quantas_horas_de_Atividades=int(input(" Digite Quantas horas de Atividades voce teve no mês"))

if Quantas_horas_de_Atividades <=10:

    Pontos=Quantas_horas_de_Atividades* 2

    faturamento_em_dinheiro = Pontos * 0.05

    print(" Quantidades de horas de Atividade é de ",Quantas_horas_de_Atividades)

    print(" voce tem ",Pontos,"  pontos e o Faturamento é de ",faturamento_em_dinheiro)

if Quantas_horas_de_Atividades >10 and Quantas_horas_de_Atividades <=20 :
    
    Pontos = Quantas_horas_de_Atividades * 5

    faturamento_em_dinheiro = Pontos * 0.05

    print(" A Quantidade de horas de Atividade é de ",Quantas_horas_de_Atividades )

    print(" voce tem " ,Pontos, " Pontos e o valor do faturamento é de ", faturamento_em_dinheiro)

elif Quantas_horas_de_Atividades > 20 :
    
    Pontos = Quantas_horas_de_Atividades * 10

    faturamento_em_dinheiro = Pontos * 0.05

    print(" voce tem ",Pontos," Pontos e o Faturamento é de ",faturamento_em_dinheiro)