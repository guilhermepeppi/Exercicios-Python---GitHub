# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(f'Os números em ordem decrescente são: {numero1}, {numero2}, {numero3}')
    else:
        print(f'Os números em ordem decrescente são: {numero1}, {numero3}, {numero2}')
elif numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print(f'Os números em ordem decrescente são: {numero2}, {numero1}, {numero3}')
    else:
        print(f'Os números em ordem decrescente são: {numero2}, {numero3}, {numero1}')
else:
    if numero1 > numero2:
        print(f'Os números em ordem decrescente são: {numero3}, {numero1}, {numero2}')
    else:
        print(f'Os números em ordem decrescente são: {numero3}, {numero2}, {numero1}')
