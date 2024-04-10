# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
# metodologia da tabelinha, que já é um sucesso na sua loja de 1,99.

# Você foi contratado para desenvolver o programa que monta a tabela de preços
# de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário,
# conforme o exemplo abaixo:

# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

def linhas(tamanho=50):
    return ('-' * tamanho)


def cabecalho():
    print(linhas())
    print('Panificadora Pão de Ontem - Tabela de preços'.center(50))
    print(linhas())


cabecalho()

qtde_paes = 50

while True:
    try:
        valor_pao = float(input('Valor do pão: R$'))
        break
    except ValueError:
        print('Digite um valor válido.')

for i in range(1, qtde_paes+1):
    print(f'{i} - R${valor_pao*i:.2f}'.replace('.', ','))
