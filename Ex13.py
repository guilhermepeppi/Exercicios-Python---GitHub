# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

altura = float(input('Digite a sua altura: '))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7
print(f'O peso ideal para uma pessoa com {altura:.2f}m de altura é:')
print(f'Para homens: {peso_ideal_homem:.2f}kg.')
print(f'Para mulheres: {peso_ideal_mulher:.2f}kg.')
