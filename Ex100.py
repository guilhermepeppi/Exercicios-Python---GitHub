# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
# a soma dos quadrados dos elementos do vetor.

vetor = []
soma = 0

for i in range(10):
    while True:
        try:
            numero = int(input(f'{i+1}º número: '))
            vetor.append(numero)
            soma += (numero**2)
            break
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro.\033[m')

print(f"Soma dos quadrados dos elementos do vetor: {soma:.2f}")
