# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
# seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
# valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela abaixo: Quantidade de
# Parcelas % de Juros sobre o valor inicial da dívida 1 0 3 10 6 15 9 20 12 25

# Exemplo de saída do programa: Valor da Dívida Valor dos Juros Quantidade de
# Parcelas Valor da Parcela R$ 1.000,00 0 1 R$ 1.000,00 R$ 1.100,00 100 3 R$
# 366,00 R$ 1.150,00 150 6 R$ 191,67

divida = float(input("Digite o valor da dívida: R$ "))

tabela_parcelas = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
for parcela, juros in tabela_parcelas:
    valor_juros = divida * (juros / 100)
    divida_com_juros = divida + valor_juros
    valor_parcela = divida_com_juros / parcela
    print(f"R$ {divida_com_juros:.2f}        | R$ {valor_juros:.2f}            | \
          {parcela}                     | R$ {valor_parcela:.2f}")
