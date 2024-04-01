# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Farenheit.

celsius = float(input('Digite a temperatura em graus Celsius: '))
farenheit = (celsius * 9 / 5) + 32
print(f'A temperatura de {celsius:.2f} graus Celsius equivale a {farenheit:.2f} graus Farenheit.')
