# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo.
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = float(input('Digite o número real: '))
produto = (num1 * 2) * (num2 / 2)
soma = (num1 * 3) + num3
cubo = num3 ** 3
print(f'O produto do dobro do primeiro com metade do segundo é {produto}.')
print(f'A soma do triplo do primeiro com o terceiro é {soma}.')
print(f'O terceiro elevado ao cubo é {cubo:.2f}.')
