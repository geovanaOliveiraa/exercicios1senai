num = input("Digite um número inteiro de três dígitos: ")

if len(num) != 3 or not num.isdigit():
    print("Número inválido")
else:
    digit.sum = int(num[0]) + int(num[1]) + int(num[2])
    print("A soma dos dígitos é:", digit.sum)
