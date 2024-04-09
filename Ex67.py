# Faça um programa que mostre todos os primos entre 1 e N sendo N um número
# inteiro fornecido pelo usuário.

# O programa deverá mostrar também o número de divisões que ele executou para
# encontrar os números primos.

# Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
# executados.

# Solicita ao usuário que digite um número inteiro
numero = int(input('Digite um número: '))

# Inicializa uma variável para contar o número de números primos encontrados
primo = 0

# Itera sobre cada número de 1 até o número fornecido pelo usuário
for i in range(1, numero + 1):
    # Inicializa uma variável para contar o número de divisões
    divisoes = 0
    # Itera sobre cada número de 1 até o número atual (i)
    for j in range(1, i + 1):
        # Verifica se i é divisível por j
        if i % j == 0:
            # Se sim, incrementa o contador de divisões
            divisoes += 1
    # Se o número de divisões for exatamente 2, então o número é primo
    if divisoes == 2:
        # Imprime o número primo
        print(i)
        # Incrementa o contador de números primos encontrados
        primo += 1

# Imprime o número total de divisões realizadas
print(f'Número de divisões: {primo}')
