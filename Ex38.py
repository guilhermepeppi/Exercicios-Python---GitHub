# Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário o valor do saque
# e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1:
# Para sacar a quantia de 256 reais:
# o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# Exemplo 2:
# Para sacar a quantia de 399 reais:
# o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = int(input("Digite o valor do saque: "))  # Solicita ao usuário o valor do saque e converte para um número inteiro.
notas = [100, 50, 10, 5, 1]  # Lista contendo os valores das notas disponíveis.
quantidade = [0, 0, 0, 0, 0]  # Lista para armazenar a quantidade de cada nota que será fornecida.

if valor_saque < 10 or valor_saque > 600:  # Verifica se o valor do saque está dentro do intervalo permitido.
    print("Valor inválido")  # Se estiver fora do intervalo, exibe uma mensagem de valor inválido.
else:
    for i in range(5):  # Loop para calcular a quantidade de cada nota necessária para o saque.
        quantidade[i] = valor_saque // notas[i]  # Calcula quantas notas de determinado valor são necessárias.
        valor_saque = valor_saque % notas[i]  # Calcula o valor restante após retirar as notas necessárias.

    # Exibe a quantidade de cada nota que será fornecida.
    print(f"Notas de 100: {quantidade[0]}")
    print(f"Notas de 50: {quantidade[1]}")
    print(f"Notas de 10: {quantidade[2]}")
    print(f"Notas de 5: {quantidade[3]}")
    print(f"Notas de 1: {quantidade[4]}")
