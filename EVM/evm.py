def calculate_avm():
    """
    Program to calculate the cost of each sprint of tbl based in EVMAgile.
    """

    # Points Completed
    PC = int(input("Insira os pontos completados nessa sprint (PC): "))

    # Planned Store Points
    PSP = int(input("Insira os pontos planejados na release (PSP): "))

    # Story Points Completed
    SPC = int(input("Insira os pontos completados da release (SPC): "))

    # Expected Percent Complete
    sprint = int(input("Insira o número de sprints completadas: "))
    sprints = int(input("Insira o número de sprints da release: "))
    EPC = sprint/sprints

    # Point cost
    estimate = float(input("Insira o orçamento do projeto: "))
    price_per_hour = float(input("Insira o preço do profissional por hora de trabalho: "))
    members_number = float(input("Insira o número de membros trabalhando nessa sprint: "))

    # Atual Percent Complete
    APC = SPC/PSP

    print("\n")
    print("Pontos completados (PC):", PC)
    print("Pontos planejados na release (PSP):", PSP)
    print("Pontos completados na release atualmente (SPC):", SPC)
    print("Porcentagem de sprints planejadas e completadas (EPC): %d percent" % (EPC * 100))
    print("Porcentagem de issues Planejadas e completadas (APC): %d percent" % (APC * 100))

    # Point Cost
    CP = price_per_hour * members_number
    print("Custo por pontos estimados (CP): R$ %.2f" % CP)

    # Budget At Complete
    BAC = PSP * CP
    print("Orçamento do projeto (BAC): R$ %.2f" % BAC)

    # Actual Cost
    AC = SPC * CP
    print("Custo atual do projeto (AC): R$ %.2f" % AC)

    # Earned Value
    EV = APC * BAC
    print("Valor ganho no momento (EV): R$ %.2f" % EV)

    if EV > AC:
        print("Excelente: O valor ganho está acima do custo atual.")
    elif EV == AC:
        print("Bom: O valor ganho está de acordo com o custo atual.")
    else:
        print("Ruim: O custo está maior que o valor ganho no projeto.")

    # Planned Value
    PV = EPC * BAC
    print("Valor planejado até o momento (PV): R$ %.2f" % PV)

    if EV > PV:
        print("Excelente: O valor ganho está acima do valor planejado.")
    elif EV == PV:
        print("Bom: O valor ganho está de acordo com o custo planejado.")
    else:
        print("Ruim: O valor planejado está maior que o valor ganho no projeto.")

    # Cost Variance
    CV = EV - AC
    print("Variação de custo (CV): %.2f" % CV)

    if CV > 0:
        print("Parabéns você está gerando lucro acima dos custos do projeto.")
    elif CV == 0:
        print("O projeto está andando alinhado com os custos.")
    else:
        print("Os custos estão acima do valor ganho no projeto.")

    # Squedule Variance
    SV = EV - PV
    print("Variação de planejamento (SV): %.2f" % SV)

    if SV > 0:
        print("Parabéns você fez tudo o que planejou fazer e um pouco mais.")
    elif SV == 0:
        print("Você conseguiu fazer tudo que planejou.")
    else:
        print("Você está atrasado de acordo com o planejamento.")

    # Cost Performance Index
    CPI = EV/AC
    print("Indice de performace de custo (CPI): %.2f" % CPI)

    if CPI > 1:
        print("Excelente: Custo abaixo do orçamento.")
    elif CPI == 1:
        print("Bom: Custo está no orçamento.")
    else:
        print("Ruim: Custo acima do orçamento.")

    # Planned Performance Index
    SPI = EV/PV
    print("Indice de performace de planejamento (SPI): %.2f" % SPI)

    if SPI > 1:
        print("Excelente: O projeto está a frente do previsto.")
    elif SPI == 1:
        print("Bom: O projeto está de acordo com o planejado.")
    else:
        print("Ruim: O projeto está atrasado.")


if __name__ == '__main__':
    calculate_avm()
