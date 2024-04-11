# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
# foram lidas. Imprima as consoantes.


vetor = []
total_consoantes = 0

for i in range(1, 11):
    try:
        caracteres = input(f'Digite o {i}º caractere: ')
        vetor.append(caracteres)
    except:
        print('\033[31mERRO! Digite um valor válido.\033[m')

for index, consoante in enumerate(vetor):
    if consoante not in 'aeiou':
        total_consoantes += 1
        if index == len(vetor) - 1:
            print(consoante + '.', end='')
        else:
            print(consoante + ',', end='')


print(f'\nQuantidade de consoantes: {total_consoantes}')
