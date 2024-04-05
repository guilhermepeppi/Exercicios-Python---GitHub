# Faça um programa que, dado um conjunto de N números, determine o menor valor,
# o maior valor e a soma dos valores.

valores = []

numero = int(input('Digite um número inteiro: '))
valores.append(numero)

while True:
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'S':
        numero = int(input('Digite um número inteiro: '))
        valores.append(numero)
    elif continuar == 'N':
        break
    else:
        print('Opção inválida. Tente novamente.')

print(f'O menor valor é: {min(valores)}')
print(f'O maior valor é: {max(valores)}')
print(f'A soma dos valores é: {sum(valores)}')
