num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite sua escolha (1/2/3/4): "))


if operacao == 1:
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)
elif operacao == 2:
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)
elif operacao == 3:
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)
elif operacao == 4:
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)
else:
    print("Opção inválida. Por favor, escolha uma operação válida (1/2/3/4).")
