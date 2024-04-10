'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências.

Faça um programa que implemente uma caixa registradora rudimentar.

O programa deverá receber um número desconhecido de valores referentes aos
preços das mercadorias.

Um valor zero deve ser informado pelo operador para indicar o final da compra.

O programa deve então mostrar o total da compra e perguntar o valor em
dinheiro que o cliente forneceu, para então calcular e mostrar o valor do
troco.

Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
a próxima compra.

A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''


def linhas(tamanho=30):
    return '-' * tamanho


produto = 1
valor_total = 0
troco = 0

while True:
    try:
        valor_produto = float(input(f'Produto {produto}: R$'))
        if valor_produto == 0:
            break
        else:
            valor_total += valor_produto
            produto += 1
            continue
    except ValueError:
        print('\033[31mERRO! Digite um valor válido.\033[m')


print(linhas())

print(f'Total: R${valor_total:.2f}')

valor_recebido = float(input(f'Dinheiro: R$'))

troco = valor_recebido - valor_total

print(f'Troco: R${troco:.2f}'.replace('.', ','))
