# Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles.
# -----
# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
    soma = sum(range(num1 + 1, num2))
    print(f'A soma dos números é: {soma}')
elif num1 > num2:
    for i in range(num1 - 1, num2, -1):
        print(i)
    soma = sum(range(num1 - 1, num2, -1))
    print(f'A soma dos números é: {soma}')
else:
    print("Os números são iguais, não há intervalo.")
