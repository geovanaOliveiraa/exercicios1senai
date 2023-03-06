# Lê os três números inteiros do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Calcula a média aritmética
media = (num1 + num2 + num3) / 3

# Verifica em qual faixa a média se encontra e exibe a mensagem correspondente
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
