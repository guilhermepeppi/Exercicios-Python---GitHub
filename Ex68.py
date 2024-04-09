# Faça um programa que calcule o mostre a média aritmética de N notas.


while True:
    try:
        n = int(input('Digite a quantidade de notas: '))
        break
    except ValueError:
        print('Digite um número inteiro válido!')

soma = 0

for i in range(n):
    while True:
        try:
            nota = float(input(f'Digite a {i+1}ª nota: '))
            break
        except ValueError:
            print('Digite um número válido!')
    soma += nota

media = soma / n
print(f'A média das {n} notas é: {media:.2f}')
