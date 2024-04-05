# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

for i in range(0, 5):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print(f'A soma dos números é: {soma_numeros}')
print(f'A média dos números é: {media_numeros}')
