# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
# multiplicação e os números.

vetor = []
valor_multiplicacao = 1

for i in range(5):
    while True:
        try:
            numero = int(input(f'Digite o {i + 1}º número: '))
            vetor.append(numero)
            valor_multiplicacao = numero * valor_multiplicacao
            break
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro.\033[m')

print(f'Vetor: {vetor}')

soma = sum(vetor)

print(f'Soma do vetor: {soma}')

print(f'Multiplicação do vetor: {valor_multiplicacao}')
