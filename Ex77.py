# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que
# será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em
# 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
# usuário, conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

valor_inicial = 0
valor_final = 0

while True:
    try:
        tabuada = int(input('Tabuada do número: '))
        valor_inicial = int(input('Iniciada em: '))
        valor_final = int(input('Finalizada em: '))
        break
    except ValueError:
        print('\033[31mERRO! Digite um valor válido.\033[m')

print(f'Vou montar a tabuada de {tabuada} começando em \
      {valor_inicial} e terminando em {valor_final}:')

for i in range(valor_inicial, valor_final + 1):
    resultado = tabuada * i
    print(f'{tabuada} x {i} = {resultado}')
