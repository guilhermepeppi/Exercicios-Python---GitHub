# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(0, 5):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

maior_numero = max(numeros)

print(f'O maior número é: {maior_numero}')
