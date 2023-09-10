salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


bonus_saldo = salario_bonus (int(input ("insira o bônus: ")))

print(bonus_saldo)
