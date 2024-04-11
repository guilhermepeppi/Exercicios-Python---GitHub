# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

for i in range(1, 6):
    while True:
        try:
            numero = int(input(f'Digite o {i}º número: '))
            vetor.append(numero)
            break
        except ValueError:
            print('\033[31mERRO! Digite um valor válido.\033[m')

print(vetor)
