# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
# programa que leia as um conjunto indeterminado de temperaturas, e informe ao
# final a menor e a maior temperaturas informadas, bem como a média das
# temperaturas.

temperaturas = []
media = 0

while True:
    try:
        temperatura = input('Temperatura (digite "fim" para encerrar): ')
        if temperatura.lower() == 'fim':
            break
        temperaturas.append(float(temperatura))
        break
    except ValueError:
        print('\033[31mERRO! Digite um valor válido.\033[m')

if temperaturas:
    print(f'Valor máximo: {max(temperaturas)}')
    print(f'Valor mínimo: {min(temperaturas)}')

    media = sum(temperaturas) / len(temperaturas)

    print(f'Média de temperatura: {media:.2f}')
else:
    print('Nenhuma temperatura foi inserida.')
