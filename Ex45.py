#  Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# Até 5 Kg
# File Duplo R$4,90/kg
# Alcatra R$ 5,90 por Kg
# Picanha R$6,90/kg

# Acima de 5 Kg
# File Duplo R$5,80/kg
# Alcatra R$6,80/kg
# Picanha R$7,80/kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne
# da promoção, porém não há limites para a quantidade de carne por cliente.

# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.

# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
# e gere um cupom fiscal, contendo as informações da compra:
# tipo de carne
# quantidade de carne
# preço total
# tipo de pagamento
# valor do desconto
# valor a pagar.

tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
quantidade = float(input("Digite a quantidade em kg: "))
pagamento = input("Digite o método de pagamento (Cartão Tabajara ou outro método): ")

preco_total = 0
desconto = 0

if quantidade <= 5:
    if tipo_carne == 'File Duplo':
        preco_por_kg = 4.9
    elif tipo_carne == 'Alcatra':
        preco_por_kg = 5.9
    elif tipo_carne == 'Picanha':
        preco_por_kg = 6.9
else:
    if tipo_carne == 'File Duplo':
        preco_por_kg = 5.8
    elif tipo_carne == 'Alcatra':
        preco_por_kg = 6.8
    elif tipo_carne == 'Picanha':
        preco_por_kg = 7.8

preco_total = preco_por_kg * quantidade

if pagamento.lower() == 'cartão tabajara':
    desconto = preco_total * 0.05
    preco_total -= desconto

print("\nCupom Fiscal:")
print("Tipo de carne:", tipo_carne)
print("Quantidade:", quantidade, "kg")
print("Preço total: R$", preco_total)
print("Tipo de pagamento:", pagamento)
print("Valor do desconto: R$", desconto)
print("Valor a pagar: R$", preco_total)
