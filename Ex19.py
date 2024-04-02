# Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
else:
    print(f'{numero2} é maior que {numero1}')
