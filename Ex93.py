# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem
# inversa.

vetor = []

for i in range(1, 11):
    try:
        numero = float(input(f'Digite o {i}º número: '))
        vetor.append(numero)
    except:
        print('\033[31mERRO! Digite um valor válido.\033[m')


vetor.reverse()

print(vetor)
