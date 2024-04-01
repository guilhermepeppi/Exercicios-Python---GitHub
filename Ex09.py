# Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

farenheit = float(input('Digite a temperatura em graus Farenheit: '))
celsius = (5 * (farenheit - 32) / 9)
print(f'A temperatura de {farenheit:.2f} graus Farenheit equivale a {celsius:.2f} graus Celsius.')
