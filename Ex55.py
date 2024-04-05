# Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
elif num1 > num2:
    for i in range(num1 - 1, num2, -1):
        print(i)
else:
    print("Os números são iguais, não há intervalo.")
