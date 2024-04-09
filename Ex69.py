# Faça um programa que peça para n pessoas a sua idade, ao final o programa
# deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e
# maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

while True:
    try:
        n = int(input('Digite o número de pessoas: '))
        break
    except ValueError:
        print('Digite um número inteiro válido.')

soma = 0

while n > 0:
    try:
        idade = int(input('Digite a idade: '))
        soma += idade
        n -= 1
    except ValueError:
        print('Digite um número inteiro válido.')

media = soma / n

if media >= 0 and media <= 25:
    print('Turma jovem.')
elif media >= 26 and media <= 60:
    print('Turma adulta.')
else:
    print('Turma idosa.')
