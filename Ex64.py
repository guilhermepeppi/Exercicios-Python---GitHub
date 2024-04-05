# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
# fatorial várias vezes e limitando o fatorial a números inteiros positivos e
# menores que 16.

while True:
    numero = int(input('Digite um número inteiro: '))
    if numero > 0 and numero < 16:
        fatorial = 1

        for i in range(1, numero + 1):
            fatorial *= i
        print(f'{numero}! = {fatorial}')
        break
    else:
        print('Numero Inválido')
