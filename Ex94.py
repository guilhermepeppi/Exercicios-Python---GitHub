# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

vetor = []

for i in range(1, 5):
    try:
        numero = float(input(f'Digite o {i}º número: '))
        vetor.append(numero)
    except:
        print('\033[31mERRO! Digite um valor válido.\033[m')


print(f'Notas: {vetor}')

valor_total = sum(vetor)
media = valor_total / len(vetor)
print(f'Média: {media:.2f}')
