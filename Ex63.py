# Faça um programa que, dado um conjunto de N números, determine o menor valor,
# o maior valor e a soma dos valores.
# -----
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

valores = []

while True:
    numero = int(input('Digite um número inteiro entre 0 e 1000: '))
    if 0 <= numero <= 1000:
        valores.append(numero)
    else:
        print('Número fora do intervalo permitido. Tente novamente.')

    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Opção inválida. Tente novamente.')

if valores:
    print(f'O menor valor é: {min(valores)}')
    print(f'O maior valor é: {max(valores)}')
    print(f'A soma dos valores é: {sum(valores)}')
else:
    print('Nenhum número válido foi digitado.')
