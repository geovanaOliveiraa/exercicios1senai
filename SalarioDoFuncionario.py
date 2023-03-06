nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario <= 1500:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo.salario = salario + aumento
diferenca = novo.salario - salario

print("Novo salário de", nome, ": R$ {:.2f}".format(novo.salario))
print("Aumento de R$ {:.2f}".format(aumento))
print("Diferença em relação ao salário antigo: R$ {:.2f}".format(diferenca))
