num = int(input("Digite um número inteiro: "))


num_str = str(num)


soma = 0


for d in num_str:
    soma += int(d)**3


if soma == num:
    print(f"{num} é um número de Armstrong!")
else:
    print(f"{num} não é um número de Armstrong.")
