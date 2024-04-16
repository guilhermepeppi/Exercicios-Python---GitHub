# Faça um programa que leia uma quantidade indeterminada de números positivos e
# conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e
# [76-100].

# A entrada de dados deverá terminar quando for lido um número negativo.

contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0

while True:
    numero = int(input('Número: '))
    if numero < 0:
        break
    elif numero <= 25:
        contador_0_25 += 1
    elif numero <= 50:
        contador_26_50 += 1
    elif numero <= 75:
        contador_51_75 += 1
    elif numero <= 100:
        contador_76_100 += 1

print(f'Quantidade de números no intervalo [0-25]: {contador_0_25}')
print(f'Quantidade de números no intervalo [26-50]: {contador_26_50}')
print(f'Quantidade de números no intervalo [51-75]: {contador_51_75}')
print(f'Quantidade de números no intervalo [76-100]: {contador_76_100}')
