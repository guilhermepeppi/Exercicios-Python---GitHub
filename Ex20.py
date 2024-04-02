# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

while True:
    try:
        numero = float(input('Digite um número: '))
        break
    except ValueError:
        print('Por favor, insira um número válido.')

if numero < 0:
    print('Número negativo')
elif numero > 0:
    print('Número positivo')
else:
    print('O número é neutro')
